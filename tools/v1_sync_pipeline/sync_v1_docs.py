#!/usr/bin/env python3
"""Fetch Affinity v1 docs HTML, convert to markdown, and save artifacts."""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Dict, List, Tuple
from urllib.parse import urljoin

import requests
import yaml
from bs4 import BeautifulSoup, NavigableString, Tag

AFFINITY_V1_URL = "https://api-docs.affinity.co/"
RAW_MARKDOWN_URL = "https://raw.githubusercontent.com/yaniv-golan/affinity-api-docs/main/docs/v1/affinity_api_docs.md"
# Temporary workarounds for known broken in-page anchors on the live site (confirmed 2025-11-06).
# When Affinity fixes these IDs, we simply won't hit these mappings because the original anchors
# will be discoverable in `self.anchor_ids`.
BROKEN_ANCHOR_MAP = {
    "retrieving-field-values": "get-field-values",
    "fetch-a-relationship-strength": "get-relationship-strength",
}
PILL_BADGES = {
    "List Entry": ("https://img.shields.io/badge/List%20Entry-orange", "orange"),
    "Global Field": ("https://img.shields.io/badge/Global%20Field-blue", "blue"),
    "List-specific Field": ("https://img.shields.io/badge/List--specific%20Field-red", "red"),
    "Field Value": ("https://img.shields.io/badge/Field%20Value-purple", "purple"),
    "Smart Field Value": ("https://img.shields.io/badge/Smart%20Field%20Value-green", "green"),
}


def normalize_text(text: str) -> str:
    """Normalize curly quotes, em dashes, and whitespace."""
    replacements = {
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2014": "--",
        "\xa0": " ",
    }
    for bad, good in replacements.items():
        text = text.replace(bad, good)
    text = re.sub(r"[\t\r\f]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


def normalize_code(text: str) -> str:
    replacements = {
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
    }
    for bad, good in replacements.items():
        text = text.replace(bad, good)
    return text


@dataclass
class CodeSample:
    language: str
    code: str
    section: str


@dataclass
class SectionRecord:
    title: str
    anchor: str
    markdown: str


def slugify(title: str) -> str:
    slug = title.strip().lower()
    slug = slug.replace(" ", "-")
    slug = slug.replace("/", "-")
    slug = re.sub(r"[^\w-]", "", slug)
    return slug


SKIP_TOC_TITLES = {
    "example request",
    "example response",
    "parameters",
    "path parameters",
    "query parameters",
    "payload parameters",
    "body parameters",
    "returns",
    "return",
    "note",
}


def build_toc(markdown_body: str) -> str:
    toc_lines: List[str] = []
    in_code = False
    slug_counts: Dict[str, int] = {}
    for line in markdown_body.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        match = re.match(r"^(#{1,6})\s+(.*)", line)
        if not match:
            continue
        level = len(match.group(1))
        title = match.group(2).strip()
        if level > 4:
            continue
        normalized = title.lower()
        if normalized in SKIP_TOC_TITLES or normalized.startswith("example "):
            continue
        if normalized == "spacer":
            continue
        base = slugify(title)
        count = slug_counts.get(base, 0)
        slug_counts[base] = count + 1
        anchor = base if count == 0 else f"{base}-{count}"
        indent = "  " * (level - 1)
        toc_lines.append(f"{indent}- [{title}](#{anchor})")
    return "\n".join(toc_lines)


def render_header(args, timestamp: datetime, snapshot_path: Path, toc: str) -> str:
    long_ts = timestamp.strftime("%B %d, %Y at %H:%M:%S %Z")
    short_ts = timestamp.strftime("%m/%d/%Y %H:%M:%S %Z")
    header_lines = [
        "# Affinity API v1 Documentation (Auto-synced)",
        "",
        "> **⚠️ IMPORTANT DISCLAIMER**",
        ">",
        "> **This is an UNOFFICIAL markdown copy of the Affinity API v1 documentation.** The official and authoritative documentation is maintained by Affinity at:",
        ">",
        f"> **📚 Official Documentation:** [{args.url}]({args.url})",
        ">",
        "> **Always refer to the official Affinity documentation for the most up-to-date and accurate information.**",
        "",
        "---",
        "",
        "## About This Document",
        "",
        "This markdown version of the Affinity API v1 documentation was generated automatically to provide:",
        "",
        "- **Better compatibility with AI coding assistants**",
        "- **Offline access**",
        "- **Text-based search**",
        "- **Version control**",
        "- **Direct raw access**",
        "",
        f"**Source:** Extracted from the live Affinity API documentation at {args.url}",
        f"**Documentation Version:** This copy is based on the official documentation as it appeared on **{long_ts}** (Last updated: {short_ts}).",
        f"**Raw Markdown URL:** `{RAW_MARKDOWN_URL}`",
        "",
        "> **⚠️ Use at Your Own Risk**",
        ">",
        "> While every effort is made to ensure accuracy, this is an unofficial copy and may contain errors or outdated information.",
        "",
        "## Contact & Support",
        "",
        "- **Affinity Support:** [support@affinity.co](mailto:support@affinity.co)",
        f"- **Official v1 Documentation:** [{args.url}]({args.url})",
        "- **Official v2 Documentation:** [https://developer.affinity.co/](https://developer.affinity.co/)",
        "",
        "---",
        "",
        "## Table of Contents",
        "",
        toc,
        "",
    ]
    return "\n".join(header_lines)


def move_examples_below_details(markdown: str) -> str:
    """Ensure Example Request/Response blocks come after endpoint descriptions."""

    def collect_example_block(body_lines: List[str], start: int) -> tuple[List[str], int]:
        idx = start
        captured: List[str] = []
        while idx < len(body_lines) and body_lines[idx].startswith("#### Example"):
            captured.append(body_lines[idx])
            idx += 1
            # capture optional blank line after heading
            while idx < len(body_lines) and body_lines[idx].strip() == "" and not captured[-1].strip() == "":
                captured.append(body_lines[idx])
                idx += 1
            fence_open = False
            while idx < len(body_lines):
                line = body_lines[idx]
                captured.append(line)
                if line.startswith("```"):
                    fence_open = not fence_open
                    if not fence_open:
                        idx += 1
                        break
                idx += 1
            while idx < len(body_lines) and body_lines[idx].strip() == "":
                captured.append(body_lines[idx])
                idx += 1
        return captured, idx

    def reorder_section(section_lines: List[str]) -> List[str]:
        header = section_lines[0]
        body = section_lines[1:]
        idx = 0
        while idx < len(body) and body[idx].strip() == "":
            idx += 1
        if idx >= len(body) or not body[idx].startswith("#### Example"):
            return section_lines
        example_lines, next_idx = collect_example_block(body, idx)
        if not example_lines:
            return section_lines
        remaining = body[:idx] + body[next_idx:]
        while remaining and remaining[0].strip() == "":
            remaining = remaining[1:]
        new_section: List[str] = [header]
        if not remaining or remaining[0].strip() != "":
            new_section.append("\n")
        new_section.extend(remaining)
        if new_section and new_section[-1].strip() != "":
            new_section.append("\n")
        while example_lines and example_lines[0].strip() == "":
            example_lines = example_lines[1:]
        while example_lines and example_lines[-1].strip() == "":
            example_lines = example_lines[:-1]
        if example_lines:
            if not new_section or new_section[-1].strip() != "":
                new_section.append("\n")
            new_section.extend(example_lines)
            if not new_section[-1].endswith("\n"):
                new_section.append("\n")
        return new_section

    lines = markdown.splitlines(keepends=True)
    result: List[str] = []
    section: List[str] = []
    in_section = False

    for line in lines:
        if (line.startswith("# ") or line.startswith("## ")) and not line.startswith("### "):
            if in_section:
                result.extend(reorder_section(section))
                section = [line]
            else:
                if section:
                    result.extend(section)
                section = [line]
                in_section = True
            continue
        if in_section:
            section.append(line)
        else:
            result.append(line)
    if section:
        if in_section:
            result.extend(reorder_section(section))
        else:
            result.extend(section)
    return "".join(result)


CODE_BLOCK_PATTERN = re.compile(r"```[^\n]*\n(.*?)```", re.S)


def load_example_overrides(path: Path) -> Dict[str, Dict[str, str]]:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text()) or {}
    overrides: Dict[str, Dict[str, str]] = {}
    for anchor, payload in data.items():
        overrides[anchor] = payload or {}
    return overrides


def apply_overrides_and_validate(parser: "AffinityV1Parser", overrides: Dict[str, Dict[str, str]]) -> Tuple[str, List[Dict[str, str]]]:
    updated_sections: List[SectionRecord] = []
    mismatches: List[Dict[str, str]] = []

    for section in parser.section_records:
        text = section.markdown
        override = overrides.get(section.anchor)
        if override:
            text = apply_override_to_section(text, override)
        mismatch = validate_section_examples(section, text)
        if mismatch:
            mismatches.append(mismatch)
        updated_sections.append(SectionRecord(section.title, section.anchor, text))

    parser.section_records = updated_sections
    parts = []
    if parser.preface_markdown.strip():
        parts.append(parser.preface_markdown.rstrip())
    parts.extend(sec.markdown.rstrip() for sec in parser.section_records if sec.markdown.strip())
    combined = "\n\n".join(parts)
    return combined, mismatches


def apply_override_to_section(section_text: str, override: Dict[str, str]) -> str:
    text = section_text
    if "example_request" in override:
        text = replace_example_block(text, "Request", override["example_request"] or "")
    if "example_response" in override:
        text = replace_example_block(text, "Response", override["example_response"] or "")
    return text


def replace_example_block(text: str, label: str, new_content: str) -> str:
    heading = f"#### Example {label}"
    pattern = re.compile(rf"^\s*{heading}\n(?:\n)?```.*?```", re.S | re.MULTILINE)
    text = pattern.sub("", text)
    new_content = (new_content or "").strip()
    if not new_content:
        return text
    replacement = f"{heading}\n\n{new_content}\n"
    text = text.rstrip() + "\n\n" + replacement
    return text


def validate_section_examples(section: SectionRecord, section_text: str) -> Dict[str, str] | None:
    declared = extract_declared_endpoint(section_text)
    example = extract_first_example(section_text)
    if not declared or not example:
        return None
    expected_method, expected_path = declared
    example_method, example_path = example
    if example_method == expected_method and paths_match(expected_path, example_path):
        return None
    return {
        "anchor": section.anchor,
        "title": section.title,
        "expected_method": expected_method,
        "expected_path": expected_path,
        "example_method": example_method,
        "example_path": example_path,
    }


def extract_declared_endpoint(section_text: str) -> Tuple[str, str] | None:
    inline = re.search(r"`(GET|POST|PUT|DELETE|PATCH)\s+(/[^`\s]+)`", section_text)
    if not inline:
        inline = re.search(r"\b(GET|POST|PUT|DELETE|PATCH)\s+(/[^\s`]+)", section_text)
    if not inline:
        return None
    return inline.group(1), inline.group(2)


def extract_first_example(section_text: str) -> Tuple[str, str] | None:
    for block in CODE_BLOCK_PATTERN.finditer(section_text):
        body = block.group(1)
        if "curl" not in body:
            continue
        url_match = re.search(r"\"https://api\\.affinity\\.co([^\"\s]*)\"", body)
        if not url_match:
            continue
        method_match = re.search(r"-(?:-request|X)\s+\"?([A-Z]+)\"?", body, re.IGNORECASE)
        method = method_match.group(1).upper() if method_match else "GET"
        path = url_match.group(1) or "/"
        path = path.split("?")[0] or "/"
        if not path.startswith("/"):
            path = f"/{path}"
        return method, path
    return None


def paths_match(expected: str, actual: str) -> bool:
    expected_clean = expected.split("?")[0]
    actual_clean = actual.split("?")[0]
    pattern = re.sub(r"\{[^}]+\}", r"[^/]+", expected_clean)
    pattern = "^" + pattern.rstrip("/") + "/?$"
    return re.match(pattern, actual_clean.rstrip("/")) is not None


def append_summary(summary_file: str | None, mismatches: List[Dict[str, str]]) -> None:
    if not summary_file or not mismatches:
        return
    lines = ["## Example validation warnings", ""]
    for mismatch in mismatches:
        lines.append(
            f"- `{mismatch['anchor']}` expected {mismatch['expected_method']} {mismatch['expected_path']}, "
            f"found {mismatch['example_method']} {mismatch['example_path']}"
        )
    lines.append("")
    with open(summary_file, "a", encoding="utf-8") as handle:
        handle.write("\n".join(lines))


def apply_content_hygiene(markdown: str) -> str:
    replacements = {
        "max_`{interaction type>`_date": "max_{interaction_type}_date",
        "min_`{interaction type}`_date": "min_{interaction_type}_date",
        "max interation": "max interaction",
        "min interation": "min interaction",
        "| contect |": "| content |",
    }
    for old, new in replacements.items():
        markdown = markdown.replace(old, new)

    markdown = insert_interaction_limit_note(markdown)
    markdown = annotate_reminder_requirements(markdown)
    markdown = relabel_parameter_section(markdown, "## Create a New Reminder", "Body Parameters")
    markdown = relabel_parameter_section(markdown, "## Update a Reminder", "Body Parameters")
    markdown = relabel_parameter_section(markdown, "## Upload Files", "Form Data Parameters")
    return markdown


def insert_interaction_limit_note(markdown: str) -> str:
    needle = (
        "> - One `person_id`, `organization_id` or `opportunity_id` must be specified per request.\n"
        "> - Only one `type` of interaction can be specified per request.\n"
        "> - An error will be returned if an internal person is used in the `person_id` parameter."
    )
    addition = (
        "> - `start_time` and `end_time` must be within a single one-year window when querying interactions."
    )
    if needle in markdown and addition not in markdown:
        replacement = needle.replace(
            "> - Only one `type` of interaction can be specified per request.\n",
            "> - Only one `type` of interaction can be specified per request.\n"
            + addition
            + "\n",
        )
        markdown = markdown.replace(needle, replacement)
    return markdown


def annotate_reminder_requirements(markdown: str) -> str:
    variants = [
        "Note that at most one of `person_id`, `organization_id` or `opportunity_id` can be specified per request.",
        "Note that at most one of `person_id`, `organization_id` or `opportunity_id` can be specified.",
    ]
    addition = (
        "One-time reminders (`type = 0`) require a `due_date`. Recurring reminders (`type = 1`) require `reset_type` and `reminder_days`."
    )
    if addition in markdown:
        return markdown
    for sentence in variants:
        if sentence in markdown:
            markdown = markdown.replace(sentence, f"{sentence}\n\n{addition}", 1)
            break
    return markdown


def relabel_parameter_section(markdown: str, heading: str, new_label: str) -> str:
    pattern = re.compile(rf"({re.escape(heading)}[\s\S]*?)(###|####) Path Parameters", re.MULTILINE)

    def _repl(match: re.Match) -> str:
        hashes = match.group(2)
        return match.group(1) + f"{hashes} {new_label}"

    return pattern.sub(_repl, markdown, count=1)


class AffinityV1Parser:
    """Convert Affinity v1 HTML content into markdown."""

    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, "lxml")
        self.content = self.soup.select_one("div.content")
        if not self.content:
            raise RuntimeError("Unable to locate main content container in source HTML")
        self.heading_stack: List[str] = []
        self.current_section = "Root"
        self.code_samples: List[CodeSample] = []
        self.in_changelog = False
        self.anchor_ids = {
            tag.get("id")
            for tag in self.soup.find_all(attrs={"id": True})
            if tag.get("id")
        }
        self.section_records: List[SectionRecord] = []
        self.preface_markdown = ""

    # ------------------------------------------------------------------
    def build_markdown(self) -> str:
        preface_nodes: List = []
        sections: List[Dict[str, List]] = []
        current_section: Dict[str, List] | None = None

        for child in self.content.children:
            if isinstance(child, Tag) and child.name in {"h1", "h2"}:
                if current_section:
                    sections.append(current_section)
                current_section = {"heading": child, "nodes": [child]}
                continue
            target = current_section["nodes"] if current_section else preface_nodes
            target.append(child)

        if current_section:
            sections.append(current_section)

        rendered_parts: List[str] = []
        self.section_records = []
        self.preface_markdown = self.render_nodes(preface_nodes)
        if self.preface_markdown.strip():
            rendered_parts.append(self.preface_markdown)

        for section in sections:
            markdown = self.render_nodes(section["nodes"])
            if markdown.strip():
                rendered_parts.append(markdown)
            heading_tag = section["heading"]
            title = heading_tag.get_text(strip=True)
            anchor = heading_tag.get("id") or slugify(title)
            self.section_records.append(SectionRecord(title=title, anchor=anchor, markdown=markdown))

        combined = "\n\n".join(part for part in rendered_parts if part.strip())
        return combined

    def render_nodes(self, nodes: List) -> str:
        blocks: List[str] = []
        for node in nodes:
            blocks.extend(self.render_block(node))
        cleaned_blocks = [block.rstrip() for block in blocks if block and block.strip()]
        return "\n\n".join(cleaned_blocks)

    # ------------------------------------------------------------------
    def render_block(self, node) -> List[str]:  # noqa: ANN001
        if isinstance(node, NavigableString):
            text = normalize_text(str(node))
            return [text] if text.strip() else []
        if not isinstance(node, Tag):
            return []
        if node.name in {"script", "style", "nav", "header", "footer"}:
            return []

        if node.name and node.name.startswith("h") and len(node.name) == 2 and node.name[1].isdigit():
            level = int(node.name[1])
            text = self.render_inline_children(node).strip()
            if text.lower() == "spacer":
                return []
            if level == 1:
                self.in_changelog = text.lower() == "changelog"
            if self.in_changelog and level > 1:
                return [f"**{text}**"]
            lower_text = text.lower()
            if lower_text.startswith("returns"):
                heading_text = "Returns"
                self.update_heading(4, heading_text)
                blocks = [f"#### {heading_text}"]
                if lower_text != "returns":
                    blocks.append(text)
                return blocks
            self.update_heading(level, text)
            return [f"{'#' * level} {text}"]

        if node.name == "p":
            return [self.render_inline_children(node).strip()]

        if node.name == "hr":
            return ["---"]

        if node.name in {"a", "span", "strong", "em", "b", "i", "code"}:
            rendered = self.render_inline(node)
            return [rendered] if rendered else []

        if node.name == "blockquote":
            text = self.render_inline_children(node).strip()
            if text.lower() in {"example request", "example response"}:
                return [f"#### {text}"]
            return [f"> {text}"]

        if node.name == "aside":
            heading = node.find("h6")
            title = heading.get_text(strip=True) if heading else "Note"
            body_lines: List[str] = []
            for child in node.children:
                if child == heading:
                    continue
                if isinstance(child, Tag) and child.name in {"ul", "ol"}:
                    ordered = child.name == "ol"
                    li_tags = child.find_all("li", recursive=False)
                    for idx, li in enumerate(li_tags, start=1):
                        prefix = f"{idx}. " if ordered else "- "
                        body_lines.append(f"{prefix}{self.render_inline_children(li)}")
                else:
                    child_blocks = self.render_block(child)
                    for block in child_blocks:
                        for line in block.splitlines():
                            line = line.rstrip()
                            if line:
                                body_lines.append(line)
            if not body_lines:
                body_lines.append("")
            quote = "\n".join(f"> {line}" if line else ">" for line in body_lines)
            return [f"#### {title}", quote]

        if node.name == "div" and "container-pills" in node.get("class", []):
            legend_items: List[str] = []
            pills = node.find_all(class_="pill")
            for pill in pills:
                label = self.render_inline_children(pill)
                badge, color = PILL_BADGES.get(label, (None, None))
                if badge:
                    color_hint = f" ({color})" if color else ""
                    legend_items.append(f"- ![{label}]({badge}){color_hint}")
                else:
                    legend_items.append(f"- {label}")
            block = "\n".join(legend_items)
            return ["**Legend:**", block]

        if node.name == "div" and "highlight" in node.get("class", []):
            pre = node.find("pre")
            if pre:
                language = self.detect_language(pre)
                code = self.extract_code(pre)
                self.record_code_sample(language, code)
                return [self.format_code_block(language, code)]
            return []

        if node.name == "pre":
            language = self.detect_language(node)
            code = self.extract_code(node)
            self.record_code_sample(language, code)
            return [self.format_code_block(language, code)]

        if node.name == "ul":
            return [self.render_list(node, ordered=False)]

        if node.name == "ol":
            if "use-case" in node.get("class", []):
                return [self.render_use_case(node)]
            return [self.render_list(node, ordered=True)]

        if node.name == "table":
            return [self.render_table(node)]

        if node.name == "img":
            image = self.render_image(node)
            return [image] if image else []

        # Containers: recurse into children
        blocks: List[str] = []
        for child in node.children:
            blocks.extend(self.render_block(child))
        return blocks

    # ------------------------------------------------------------------
    def render_inline_children(self, node: Tag) -> str:
        parts: List[str] = []
        for child in node.children:
            parts.append(self.render_inline(child))
        text = "".join(parts)
        return normalize_text(text).strip()

    def render_inline(self, node) -> str:  # noqa: ANN001
        if isinstance(node, NavigableString):
            return str(node)
        if not isinstance(node, Tag):
            return ""
        name = node.name
        text = self.render_inline_children(node)
        if name == "code":
            anchor_child = next(
                (child for child in node.children if isinstance(child, Tag) and child.name == "a"),
                None,
            )
            if anchor_child and anchor_child.parent is node:
                href = anchor_child.get("href")
                label = normalize_text(anchor_child.get_text())
                if href:
                    if "@" in href and not href.lower().startswith(("mailto:", "http://", "https://", "#")):
                        href = f"mailto:{href}"
                    if href.startswith("#"):
                        target = href[1:]
                        if target not in self.anchor_ids and target in BROKEN_ANCHOR_MAP:
                            href = f"#{BROKEN_ANCHOR_MAP[target]}"
                return f"[`{label}`]({href})" if href else f"`{label}`"
            return f"`{text}`"
        if name in {"strong", "b"}:
            return f"**{text}**"
        if name in {"em", "i"}:
            return f"*{text}*"
        if name == "a":
            href = node.get("href")
            if href:
                if "@" in href and not href.lower().startswith(("mailto:", "http://", "https://", "#")):
                    href = f"mailto:{href}"
                if href.startswith("#"):
                    target = href[1:]
                    if target not in self.anchor_ids and target in BROKEN_ANCHOR_MAP:
                        href = f"#{BROKEN_ANCHOR_MAP[target]}"
            elif "@" in text:
                href = f"mailto:{text}"
            return f"[{text}]({href})" if href else text
        if name == "img":
            return self.render_image(node)
        if name == "span":
            css_classes = node.get("class", [])
            if any(cls.endswith("field") for cls in css_classes):
                return f"**{text}**"
            return text
        if name == "br":
            return "\n"
        return text

    # ------------------------------------------------------------------
    def render_list(self, node: Tag, ordered: bool) -> str:
        items = []
        li_tags = [li for li in node.find_all("li", recursive=False)]
        for idx, li in enumerate(li_tags, start=1):
            parts: List[str] = []
            for child in li.children:
                parts.extend(self.render_block(child))
            if not parts:
                parts.append(self.render_inline_children(li))
            text = "\n".join(part.strip() for part in parts if part.strip())
            prefix = f"{idx}. " if ordered else "- "
            item_lines = text.splitlines()
            formatted = prefix + item_lines[0]
            continuation = [f"  {line}" for line in item_lines[1:]]
            items.append("\n".join([formatted, *continuation]).strip())
        return "\n".join(items)

    # ------------------------------------------------------------------
    def render_use_case(self, node: Tag) -> str:
        # Use-case flows are represented as numbered lists for readability in markdown.
        lines: List[str] = []
        li_tags = [li for li in node.find_all("li", recursive=False)]
        for idx, li in enumerate(li_tags, start=1):
            heading = li.find("h3")
            title = self.render_inline_children(heading) if heading else "Step"
            title = re.sub(r"^\d+\.\s*", "", title)
            lines.append(f"{idx}. {title}")
            nested_ol = li.find("ol")
            if nested_ol:
                sub_lines = self.render_list(nested_ol, ordered=True)
                if sub_lines:
                    lines.append(sub_lines)
            pre = li.find("pre")
            if pre:
                code = self.extract_code(pre)
                lines.append(self.format_code_block("text", code))
        return "\n\n".join(lines)

    # ------------------------------------------------------------------
    def render_table(self, node: Tag) -> str:
        headers = []
        body_rows = []
        header_row = node.find("thead")
        if header_row:
            headers = [self.render_inline_children(th) for th in header_row.find_all("th")]
        else:
            first_row = node.find("tr")
            if first_row:
                headers = [self.render_inline_children(th) for th in first_row.find_all("th")]
        for tr in node.find_all("tr"):
            cells = [self.render_inline_children(td) for td in tr.find_all(["td", "th"])]
            if cells:
                body_rows.append(cells)
        if headers and body_rows and body_rows[0] == headers:
            body_rows = body_rows[1:]
        if not headers and body_rows:
            headers = [f"Column {idx+1}" for idx in range(len(body_rows[0]))]
        header_line = " | ".join(headers)
        divider = " | ".join(["---"] * len(headers))
        body_lines = [" | ".join(row) for row in body_rows]
        return "\n".join([f"| {header_line} |", f"| {divider} |", *[f"| {line} |" for line in body_lines]])

    # ------------------------------------------------------------------
    def detect_language(self, node: Tag) -> str:
        for cls in node.get("class", []):
            if cls.startswith("tab-"):
                return cls.replace("tab-", "")
        return node.get("data-language") or "text"

    def render_image(self, node: Tag) -> str:
        src = node.get("src")
        if not src:
            return ""
        alt = node.get("alt") or ""
        resolved = urljoin(AFFINITY_V1_URL, src)
        return f"![{alt}]({resolved})"

    def extract_code(self, node: Tag) -> str:
        code_node = node.find("code") if node.name != "code" else node
        raw = code_node.get_text("", strip=False) if code_node else node.get_text("", strip=False)
        cleaned = raw.replace("\r", "")
        cleaned = normalize_code(cleaned)
        return cleaned.strip("\n")

    def format_code_block(self, language: str, code: str) -> str:
        lang = language
        if lang in {"shell", "sh"}:
            lang = "bash"
        if lang in {"text", "plaintext"}:
            lang = ""
        fence = f"```{lang}\n{code}\n```" if lang else f"```\n{code}\n```"
        return fence

    def record_code_sample(self, language: str, code: str) -> None:
        self.code_samples.append(CodeSample(language=language, code=code, section=self.current_section))

    def update_heading(self, level: int, title: str) -> None:
        while len(self.heading_stack) < level:
            self.heading_stack.append("")
        self.heading_stack[level - 1] = title
        del self.heading_stack[level:]
        self.current_section = " > ".join(filter(None, self.heading_stack)) or "Root"


def fetch_html(url: str) -> tuple[str, str | None]:
    headers = {"User-Agent": "AffinityDocsSync/1.0 (+https://github.com)"}
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()
    return response.text, response.headers.get("Last-Modified")


def resolve_timestamp(header_value: str | None, fetched_at: datetime) -> datetime:
    if header_value:
        try:
            return parsedate_to_datetime(header_value)
        except (TypeError, ValueError):
            pass
    return fetched_at


def save_snapshot(html: str, snapshot_dir: Path, fetched_at: datetime) -> Path:
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    filename = f"v1_{fetched_at.strftime('%Y%m%dT%H%M%SZ')}.html"
    path = snapshot_dir / filename
    path.write_text(html)
    return path


def write_code_samples(samples: List[CodeSample], destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    payload = [sample.__dict__ for sample in samples]
    destination.write_text(json.dumps(payload, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync Affinity v1 docs into markdown")
    parser.add_argument("--url", default=AFFINITY_V1_URL, help="Source HTML URL")
    parser.add_argument("--output", default="docs/v1/affinity_api_docs.md", help="Output markdown path")
    parser.add_argument("--snapshot-dir", default="tmp/snapshots", help="Directory for HTML snapshots")
    parser.add_argument("--raw-html", default="tmp/api_docs_raw_sync.html", help="Latest raw HTML path")
    parser.add_argument("--code-json", default="tmp/code_blocks_sync.json", help="Where to store extracted code blocks")
    parser.add_argument("--metadata", default="tmp/v1_sync_metadata.json", help="Metadata output path")
    parser.add_argument(
        "--example-overrides",
        default="tools/v1_sync_pipeline/example_overrides.yml",
        help="Path to YAML file containing example overrides",
    )
    parser.add_argument(
        "--summary-file",
        default=None,
        help="Optional path to append warnings for GitHub summary",
    )
    parser.add_argument(
        "--fail-on-diff",
        action="store_true",
        help="Exit with status 1 if the generated markdown differs from the existing output",
    )
    args = parser.parse_args()

    fetched_at = datetime.now(timezone.utc)
    html, header_ts = fetch_html(args.url)
    snapshot_path = save_snapshot(html, Path(args.snapshot_dir), fetched_at)
    Path(args.raw_html).write_text(html)

    timestamp = resolve_timestamp(header_ts, fetched_at)
    parser_obj = AffinityV1Parser(html)
    markdown_body = parser_obj.build_markdown()
    overrides = load_example_overrides(Path(args.example_overrides))
    markdown_body, mismatches = apply_overrides_and_validate(parser_obj, overrides)
    toc = build_toc(markdown_body)
    full_markdown = render_header(args, timestamp, snapshot_path, toc) + markdown_body + "\n"
    full_markdown = move_examples_below_details(full_markdown)
    full_markdown = apply_content_hygiene(full_markdown)

    output_path = Path(args.output)
    previous_content = output_path.read_text() if output_path.exists() else None
    content_changed = previous_content != full_markdown
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(full_markdown)

    write_code_samples(parser_obj.code_samples, Path(args.code_json))

    metadata = {
        "source_url": args.url,
        "snapshot": str(snapshot_path),
        "last_modified": timestamp.isoformat(),
        "output": str(output_path),
        "example_mismatches": mismatches,
    }
    Path(args.metadata).write_text(json.dumps(metadata, indent=2))

    if mismatches:
        for mismatch in mismatches:
            print(
                f"[example-mismatch] {mismatch['anchor']}: expected {mismatch['expected_method']} {mismatch['expected_path']} "
                f"but found {mismatch['example_method']} {mismatch['example_path']}",
                file=sys.stderr,
            )

    append_summary(args.summary_file, mismatches)

    if args.fail_on_diff and content_changed:
        raise SystemExit("Generated documentation differs from existing output")


if __name__ == "__main__":
    main()
