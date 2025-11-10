"""Convert the Affinity API v2 OpenAPI spec into markdown."""
from __future__ import annotations

import copy
import json
import textwrap
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, Iterable, List, Tuple

from .utils import build_toc, normalize_whitespace, format_description, fix_mojibake, slugify


@dataclass
class RenderContext:
    source_url: str
    fetched_at: datetime
    snapshot_path: str
    info: dict[str, Any]
    spec: dict[str, Any]


class RefResolver:
    """Resolve $ref pointers and track schema usage."""

    def __init__(self, spec: dict[str, Any]):
        self.spec = spec
        self.cache: dict[str, Any] = {}
        self.used_schema_names: set[str] = set()

    def deref(self, obj: Any, *, track_schema: bool = False) -> Any:
        if isinstance(obj, dict):
            if "$ref" in obj:
                ref = obj["$ref"]
                resolved = self._resolve_pointer(ref)
                if track_schema and ref.startswith("#/components/schemas/"):
                    self.used_schema_names.add(ref.split("/")[-1])
                overrides = {
                    key: self.deref(value, track_schema=track_schema)
                    for key, value in obj.items()
                    if key != "$ref"
                }
                base = self.deref(resolved, track_schema=track_schema)
                if isinstance(base, dict):
                    merged = {**base, **overrides}
                else:
                    merged = overrides or base
                return merged
            return {key: self.deref(value, track_schema=track_schema) for key, value in obj.items()}
        if isinstance(obj, list):
            return [self.deref(item, track_schema=track_schema) for item in obj]
        return obj

    def _resolve_pointer(self, ref: str) -> Any:
        if ref not in self.cache:
            if not ref.startswith("#/"):
                raise ValueError(f"Unsupported external reference: {ref}")
            target: Any = self.spec
            for part in ref.lstrip("#/").split("/"):
                target = target[part]
            self.cache[ref] = copy.deepcopy(target)
        return copy.deepcopy(self.cache[ref])


class SpecHelper:
    """Utility helpers for rendering."""

    def __init__(self, spec: dict[str, Any]):
        self.spec = spec
        self.resolver = RefResolver(spec)
        self.tags = spec.get("tags", [])
        self.tag_order = {tag["name"]: idx for idx, tag in enumerate(self.tags)}
        servers = spec.get("servers", [{"url": "https://api.affinity.co"}])
        self.base_url = servers[0]["url"].rstrip("/")

    def iter_tagged_operations(self) -> Iterable[Tuple[str, dict[str, Any], List[dict[str, Any]]]]:
        buckets: dict[str, List[dict[str, Any]]] = {}
        untagged = "_misc"
        paths = self.spec.get("paths", {})
        for path in sorted(paths.keys()):
            for method in sorted(paths[path].keys()):
                op = paths[path][method]
                tags = op.get("tags") or [untagged]
                tag_name = tags[0]
                buckets.setdefault(tag_name, []).append(
                    {
                        "method": method.upper(),
                        "path": path,
                        "operation": op,
                        "tag": tag_name,
                    }
                )
        ordered_names = [tag["name"] for tag in self.tags if tag["name"] in buckets]
        if untagged in buckets:
            ordered_names.append(untagged)
        for name in buckets:
            if name not in ordered_names:
                ordered_names.append(name)
        for tag_name in ordered_names:
            meta = next((tag for tag in self.tags if tag["name"] == tag_name), {"name": tag_name})
            yield tag_name, meta, sorted(
                buckets[tag_name], key=lambda entry: (entry["path"], entry["method"])
            )

    def normalize_schema(self, schema: dict[str, Any] | None) -> dict[str, Any]:
        schema = schema or {}
        schema = self.resolver.deref(schema, track_schema=True)
        return self.flatten_all_of(schema)

    def flatten_all_of(self, schema: dict[str, Any]) -> dict[str, Any]:
        if "allOf" not in schema:
            return schema
        merged: dict[str, Any] = {}
        required: set[str] = set(schema.get("required", []))
        properties: dict[str, Any] = dict(schema.get("properties", {}))
        for part in schema["allOf"]:
            part_schema = self.flatten_all_of(self.resolver.deref(part, track_schema=True))
            required.update(part_schema.get("required", []))
            properties.update(part_schema.get("properties", {}))
            for key, value in part_schema.items():
                if key in {"required", "properties"}:
                    continue
                merged[key] = value
        if required:
            merged["required"] = sorted(required)
        if properties:
            merged["properties"] = properties
        for key, value in schema.items():
            if key in {"allOf", "required", "properties"}:
                continue
            merged[key] = value
        return merged

    def describe_schema_type(self, schema: dict[str, Any]) -> str:
        schema_type = schema.get("type")
        if isinstance(schema_type, list):
            schema_type = "/".join(schema_type)
        if schema_type == "array":
            item_type = self.describe_schema_type(schema.get("items", {}))
            constraints: list[str] = []
            if "maxItems" in schema:
                constraints.append(f"≤ {schema['maxItems']} items")
            if "minItems" in schema:
                constraints.append(f"≥ {schema['minItems']} items")
            extra = f" ({', '.join(constraints)})" if constraints else ""
            return f"array<{item_type}>{extra}"
        if schema_type == "object":
            return "object"
        if schema.get("enum"):
            enum_preview = ", ".join(f"`{value}`" for value in schema["enum"][:5])
            if len(schema["enum"]) > 5:
                enum_preview += ", …"
            return f"{schema_type or 'string'} (enum: {enum_preview})"
        if schema_type:
            if schema.get("format"):
                return f"{schema_type}<{schema['format']}>"
            return schema_type
        if "$ref" in schema:
            return schema["$ref"].split("/")[-1]
        if "oneOf" in schema:
            return "oneOf"
        if "anyOf" in schema:
            return "anyOf"
        return schema.get("title", "value")

    def schema_link(self, schema: dict[str, Any]) -> str | None:
        title = schema.get("title")
        if not title:
            return None
        anchor = slugify(title)
        return f"[{title}](#{anchor})"

    def describe_constraints(self, schema: dict[str, Any]) -> str:
        constraints: list[str] = []
        if "minimum" in schema:
            comparator = ">" if schema.get("exclusiveMinimum") else "≥"
            constraints.append(f"{comparator} {schema['minimum']}")
        if "maximum" in schema:
            comparator = "<" if schema.get("exclusiveMaximum") else "≤"
            constraints.append(f"{comparator} {schema['maximum']}")
        if "minLength" in schema:
            constraints.append(f"length ≥ {schema['minLength']}")
        if "maxLength" in schema:
            constraints.append(f"length ≤ {schema['maxLength']}")
        if "pattern" in schema:
            constraints.append(f"pattern: `{schema['pattern']}`")
        if "multipleOf" in schema:
            constraints.append(f"multiple of {schema['multipleOf']}")
        if "default" in schema:
            constraints.append(f"default `{schema['default']}`")
        if "x-stability-level" in schema:
            constraints.append(f"stability `{schema['x-stability-level']}`")
        return "; ".join(constraints)

    def extract_example(self, media: dict[str, Any]) -> Tuple[str | None, Any | None]:
        examples = media.get("examples")
        if isinstance(examples, dict):
            for name, example in examples.items():
                resolved = self.resolver.deref(example, track_schema=False)
                if "value" in resolved:
                    return name, resolved["value"]
        if "example" in media:
            return None, media["example"]
        schema = media.get("schema")
        if schema:
            schema = self.normalize_schema(schema)
            if "example" in schema:
                return None, schema["example"]
            if "examples" in schema and isinstance(schema["examples"], list):
                return None, schema["examples"][0]
        return None, None

    def format_markdown_table(self, rows: List[List[str]], headers: List[str]) -> str:
        table = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
        for row in rows:
            table.append("| " + " | ".join(row) + " |")
        return "\n".join(table)


class V2MarkdownRenderer:
    """Render markdown output from the v2 OpenAPI document."""

    def __init__(self, context: RenderContext):
        self.ctx = context
        self.helper = SpecHelper(context.spec)

    def build(self) -> str:
        sections: list[str] = []
        intro = self.ctx.info.get("description")
        if intro:
            sections.append(intro.strip())
        sections.append(self._render_tag_sections())
        sections.append(self._render_schema_reference())
        sections.append(self._render_error_reference())
        markdown_body = "\n\n".join([section for section in sections if section]).strip()
        toc = build_toc(markdown_body)
        header = self._render_header(toc)
        combined = f"{header}\n\n{markdown_body}".strip()
        return fix_mojibake(combined)

    def _render_header(self, toc: str) -> str:
        long_ts = self.ctx.fetched_at.strftime("%B %d, %Y at %H:%M:%S %Z")
        short_ts = self.ctx.fetched_at.strftime("%m/%d/%Y %H:%M:%S %Z")
        lines = [
            "# Affinity API v2 Documentation (Auto-synced)",
            "",
            "> **⚠️ IMPORTANT DISCLAIMER**",
            ">",
            "> **This is an UNOFFICIAL markdown copy of the Affinity API v2 documentation.** The official and authoritative documentation is maintained by Affinity at:",
            ">",
            f"> **📚 Official Documentation:** [{self.ctx.source_url}]({self.ctx.source_url})",
            ">",
            "> **Always refer to the official Affinity documentation for the most up-to-date and accurate information.**",
            "",
            "---",
            "",
            "## About This Document",
            "",
            "This markdown version of the Affinity API v2 documentation was generated automatically to provide:",
            "",
            "- **Better compatibility with AI coding assistants**",
            "- **Offline access**",
            "- **Text-based search**",
            "- **Version control**",
            "- **Direct raw access**",
            "",
            f"**Source:** Extracted from the live Affinity API documentation at {self.ctx.source_url}",
            "",
            "> **Note:** The live site renders dynamic multi-language request/response samples in-browser. Because those snippets are generated at runtime and are not embedded in the OpenAPI payload, they cannot be mirrored here. Refer to https://developer.affinity.co/ for the full interactive samples.",
            "",
            f"**Documentation Version:** This copy is based on the official documentation as it appeared on **{long_ts}** (Last updated: {short_ts}).",
            f"**Snapshot:** `{self.ctx.snapshot_path}`",
            "",
            "> **⚠️ Use at Your Own Risk**",
            ">",
            "> While every effort is made to ensure accuracy, this is an unofficial copy and may contain errors or outdated information.",
            "",
            "## Contact & Support",
            "",
            "- **Affinity Support:** [support@affinity.co](mailto:support@affinity.co)",
            f"- **Official v2 Documentation:** [{self.ctx.source_url}]({self.ctx.source_url})",
            "- **Official v1 Documentation:** [https://api-docs.affinity.co/](https://api-docs.affinity.co/)",
            "",
            "---",
            "",
            "## Table of Contents",
            "",
            toc,
        ]
        return "\n".join(lines).strip()

    def _render_tag_sections(self) -> str:
        sections: list[str] = []
        for tag_name, meta, operations in self.helper.iter_tagged_operations():
            human_name = meta.get("name", tag_name)
            if human_name == "_misc":
                human_name = "Miscellaneous"
            if human_name.startswith("#"):
                heading = human_name
            else:
                heading = f"## {human_name}"
            lines = [heading]
            description = meta.get("description")
            if description:
                formatted = format_description(description)
                if formatted:
                    lines.append("")
                    lines.append(formatted)
            for entry in operations:
                lines.append("")
                lines.append(self._render_operation(entry))
            sections.append("\n".join(lines).strip())
        return "\n\n".join(sections)

    def _render_operation(self, entry: dict[str, Any]) -> str:
        op = entry["operation"]
        summary = op.get("summary")
        title = summary or f"{entry['method']} {entry['path']}"
        heading = f"### {title}"
        stability = op.get("x-stability-level") or op.get("stability") or "beta"
        display_tag = entry["tag"] if entry["tag"] != "_misc" else "general"
        metadata_line = (
            f"- **Tag:** {display_tag} · **OperationId:** {op.get('operationId', 'n/a')} · "
            f"**Stability:** `{stability or 'beta'}` · **Auth:** bearerAuth"
        )
        lines = [heading, f"`{entry['method']} {entry['path']}`", "", metadata_line]
        description = op.get("description")
        if description:
            formatted = format_description(description)
            if formatted:
                lines.append("")
                lines.append(formatted)
        lines.extend(self._render_parameters(op))
        lines.extend(self._render_request_body(op))
        lines.extend(self._render_example_request(entry, op))
        lines.extend(self._render_responses(op))
        return "\n".join(line for line in lines if line is not None)

    def _render_parameters(self, op: dict[str, Any]) -> list[str]:
        parameters = op.get("parameters", [])
        if not parameters:
            return []
        path_rows: list[List[str]] = []
        query_rows: list[List[str]] = []
        header_rows: list[List[str]] = []
        for param in parameters:
            resolved = self.helper.resolver.deref(param, track_schema=True)
            schema = self.helper.normalize_schema(resolved.get("schema", {}))
            row = [
                f"`{resolved.get('name')}`",
                f"`{self.helper.describe_schema_type(schema)}`",
                "Yes" if resolved.get("required") else "No",
                _stringify(resolved.get("description")).replace("|", "\\|").strip(),
            ]
            location = resolved.get("in")
            if location == "path":
                path_rows.append(row)
            elif location == "query":
                query_rows.append(row)
            elif location == "header":
                header_rows.append(row)
        lines: list[str] = []

        def clean_text(raw: str | None) -> str:
            return format_description(raw or "").replace("\n", " ").strip()

        def clean_text(raw: str | None) -> str:
            return format_description(raw or "").replace("\n", " ").strip()

        def clean_text(raw: str | None) -> str:
            return format_description(raw or "").replace("\n", " ").strip()
        if path_rows:
            lines.append("")
            lines.append("#### Path Parameters")
            lines.append(self.helper.format_markdown_table(path_rows, ["Name", "Type", "Required", "Description"]))
        if query_rows:
            lines.append("")
            lines.append("#### Query Parameters")
            lines.append(self.helper.format_markdown_table(query_rows, ["Name", "Type", "Required", "Description"]))
        if header_rows:
            lines.append("")
            lines.append("#### Header Parameters")
            lines.append(self.helper.format_markdown_table(header_rows, ["Name", "Type", "Required", "Description"]))
        return lines

    def _render_request_body(self, op: dict[str, Any]) -> list[str]:
        request_body = op.get("requestBody")
        if not request_body:
            return []
        resolved_body = self.helper.resolver.deref(request_body, track_schema=True)
        content = resolved_body.get("content", {})
        if not content:
            return []
        lines = ["", "#### Request Body"]
        for media_type, media in content.items():
            schema = self.helper.normalize_schema(media.get("schema"))
            lines.append("")
            lines.append(f"**Media type:** `{media_type}`")
            rendered = self._render_schema_properties(schema, heading_level=5)
            if rendered:
                lines.append(rendered)
            name, example = self.helper.extract_example(media)
            if example is not None:
                label = f"Example: {name}" if name else "Example"
                lines.append("")
                lines.append(f"{label}")
                lines.append("```json")
                lines.append(json.dumps(example, indent=2, sort_keys=True, ensure_ascii=False))
                lines.append("```")
        return lines

    def _render_example_request(self, entry: dict[str, Any], op: dict[str, Any]) -> list[str]:
        method = entry["method"]
        path = entry["path"]
        example_body = None
        request_body = op.get("requestBody")
        if request_body:
            resolved_body = self.helper.resolver.deref(request_body, track_schema=True)
            content = resolved_body.get("content", {})
            if content:
                first_media = next(iter(content.values()))
                _, example_body = self.helper.extract_example(first_media)
        curl_lines = [
            f"curl --request {method} '{self.helper.base_url}{path}'",
            "  --header 'Authorization: Bearer YOUR_API_KEY'",
        ]
        if example_body is not None:
            curl_lines.append("  --header 'Content-Type: application/json'")
            payload = json.dumps(example_body, separators=(",", ":"), ensure_ascii=False)
            curl_lines.append(f"  --data-raw '{_bash_quote(payload)}'")
        return ["", "#### Example Request", "", "```bash", " \\\n".join(curl_lines), "```"]

    def _render_responses(self, op: dict[str, Any]) -> list[str]:
        responses = op.get("responses", {})
        if not responses:
            return []
        lines = ["", "#### Responses"]
        for status, response in sorted(responses.items(), key=_response_sort_key):
            resolved_resp = self.helper.resolver.deref(response, track_schema=True)
            description = resolved_resp.get("description", "").strip()
            lines.append("")
            heading = f"##### {status.upper()}"
            media_content = resolved_resp.get("content", {})
            if media_content:
                media_label = ", ".join(media_content.keys())
                heading += f" — {media_label}"
            lines.append(heading)
            if description:
                lines.append("")
                lines.append(description)
            for media_type, media in media_content.items():
                schema = self.helper.normalize_schema(media.get("schema"))
                lines.append("")
                lines.append(f"**Response schema (`{media_type}`):**")
                schema_heading = schema.get("title")
                schema_type = self.helper.describe_schema_type(schema)
                heading_title = schema_heading or schema_type
                lines.append(f"###### Schema: {heading_title}")
                lines.append(f"*Type:* {schema_type}")
                rendered = self._render_schema_properties(schema, heading_level=6)
                if rendered:
                    lines.append(rendered)
                name, example = self.helper.extract_example(media)
                if example is not None:
                    label = f"Example: {name}" if name else "Example"
                    lines.append("")
                    lines.append(label)
                    lines.append("")
                    lines.append("```json")
                    lines.append(json.dumps(example, indent=2, sort_keys=True, ensure_ascii=False))
                    lines.append("```")
            headers = resolved_resp.get("headers")
            if headers:
                header_rows = []
                for header_name, header in headers.items():
                    header_schema = self.helper.normalize_schema(header.get("schema"))
                    header_rows.append(
                        [
                            f"`{header_name}`",
                            f"`{self.helper.describe_schema_type(header_schema)}`",
                            _stringify(header.get("description")).replace("|", "\\|").strip(),
                        ]
                    )
                lines.append("")
                lines.append("**Response Headers**")
                lines.append(self.helper.format_markdown_table(header_rows, ["Header", "Type", "Description"]))
        return lines

    def _render_schema_properties(self, schema: dict[str, Any], heading_level: int = 4) -> str:
        lines: list[str] = []

        def clean_text(raw: str | None) -> str:
            return format_description(raw or "").replace("\n", " ").strip()
        description = schema.get("description")
        title = schema.get("title", "")
        if description and title:
            desc_norm = description.strip().lower()
            title_norm = title.split(".")[-1].strip().lower()
            if desc_norm in {title_norm, f"{title_norm} model"}:
                description = ""
        if description:
            lines.append(format_description(description))
        schema_type = schema.get("type")
        nested_sections: list[str] = []
        if schema_type == "object" and schema.get("properties"):
            rows = []
            required = set(schema.get("required", []))
            for prop, details in schema["properties"].items():
                prop_schema = self.helper.normalize_schema(details)
                desc_text = format_description(prop_schema.get("description", "")).replace("\n", " ").strip()
                constraints = self.helper.describe_constraints(prop_schema)
                if constraints:
                    constraint_text = f"(Constraints: {constraints})"
                    desc_text = f"{desc_text} {constraint_text}".strip()
                rows.append(
                    [
                        f"`{prop}`",
                        f"`{self.helper.describe_schema_type(prop_schema)}`",
                        "Yes" if prop in required else "No",
                        desc_text.replace("|", "\\|"),
                    ]
                )
                child_schema_type = prop_schema.get("type")
                child_types = set(child_schema_type) if isinstance(child_schema_type, list) else {child_schema_type}
                if (
                    bool(child_types & {"object", "array"})
                    or "properties" in prop_schema
                    or "items" in prop_schema
                ):
                    nested_schema = prop_schema
                    if prop_schema.get("description"):
                        nested_schema = dict(prop_schema)
                        nested_schema.pop("description", None)
                    nested = self._render_schema_properties(nested_schema, heading_level=heading_level + 1)
                    if nested:
                        detail_parts: list[str] = []
                        link = self.helper.schema_link(prop_schema)
                        if not link and prop_schema.get("type") == "array" and prop_schema.get("items"):
                            items_schema = prop_schema["items"]
                            link = self.helper.schema_link(items_schema)
                            if not detail_parts and items_schema.get("description"):
                                detail_parts.append(clean_text(items_schema.get("description")))
                        if link:
                            detail_parts.append(f"See {link}")
                        elif prop_schema.get("description"):
                            detail_parts.append(clean_text(prop_schema.get("description")))
                        preface = f"**`{prop}` details**"
                        if detail_parts:
                            preface = f"{preface} — {' '.join(detail_parts)}"
                        nested_sections.append(f"{preface}\n\n{nested}")
            lines.append("")
            lines.append("**Properties**")
            lines.append(self.helper.format_markdown_table(rows, ["Field", "Type", "Required", "Description"]))
        if schema_type == "array" and schema.get("items"):
            item_schema = self.helper.normalize_schema(schema["items"])
            item_schema = dict(item_schema)
            item_schema.pop("description", None)
            nested_sections.append(
                f"**Items**\n\n{self._render_schema_properties(item_schema, heading_level=heading_level + 1)}"
            )
        if "enum" in schema:
            enum_values = ", ".join(f"`{value}`" for value in schema["enum"])
            lines.append("")
            lines.append(f"Allowed values: {enum_values}")
        if "oneOf" in schema:
            for idx, option in enumerate(schema["oneOf"], start=1):
                variant = self.helper.normalize_schema(option)
                title = variant.get("title") or f"Option {idx}"
                lines.append("")
                lines.append(f"**Variant:** {title}")
                lines.append(self._render_schema_properties(variant, heading_level=heading_level + 1))
        if "anyOf" in schema:
            for idx, option in enumerate(schema["anyOf"], start=1):
                variant = self.helper.normalize_schema(option)
                title = variant.get("title") or f"Option {idx}"
                lines.append("")
                lines.append(f"{'#' * heading_level} Variant: {title}")
                lines.append(self._render_schema_properties(variant, heading_level=heading_level + 1))
        block = "\n".join(line for line in lines if line).strip()
        if nested_sections:
            block = "\n\n".join([block] + nested_sections)
        return block.strip()

    def _render_schema_reference(self) -> str:
        used = sorted(self.helper.resolver.used_schema_names)
        if not used:
            return ""
        sections = ["## Schema Reference"]
        schemas = self.ctx.spec.get("components", {}).get("schemas", {})
        for name in used:
            schema = schemas.get(name)
            if not schema:
                continue
            normalized = self.helper.normalize_schema(schema)
            sections.append("")
            sections.append(f"### {name}")
            description = normalized.get("description")
            if description:
                sections.append("")
                sections.append(format_description(description))
            rendered = self._render_schema_properties(normalized, heading_level=4)
            if rendered:
                sections.append("")
                sections.append(rendered)
        return "\n".join(section for section in sections if section).strip()

    def _render_error_reference(self) -> str:
        error_schema = (
            self.ctx.spec.get("components", {})
            .get("schemas", {})
            .get("Error")
        )
        if not error_schema:
            return ""
        normalized = self.helper.normalize_schema(error_schema)
        discriminator = normalized.get("discriminator", {})
        mapping = discriminator.get("mapping", {})
        if not mapping:
            return ""
        lines = ["## Error Reference", "", "The API returns structured errors with a `code` discriminator."]
        rows = []
        for code, ref in sorted(mapping.items()):
            rows.append([f"`{code}`", ref.split("/")[-1]])
        lines.append(self.helper.format_markdown_table(rows, ["Error Code", "Schema"]))
        return "\n".join(lines)


def _response_sort_key(item: Tuple[str, Any]) -> Tuple[int, str]:
    status, _ = item
    if status.isdigit():
        return (0, f"{int(status):03d}")
    if status.lower() == "default":
        return (2, status)
    return (1, status)


def _bash_quote(value: str) -> str:
    """Escape single quotes for use inside a single-quoted bash string."""
    return value.replace("'", "'\"'\"'")


def _stringify(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False)
    return str(value)
