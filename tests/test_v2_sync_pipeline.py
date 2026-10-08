"""Tests for the Affinity API v2 sync pipeline."""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import re
import sys

import pytest
import requests

from tools.v2_sync_pipeline import openapi_loader
from tools.v2_sync_pipeline import site_pages
from tools.v2_sync_pipeline import sync_v2_docs
from tools.v2_sync_pipeline.markdown_renderer import (
    RefResolver,
    RenderContext,
    V2MarkdownRenderer,
    rewrite_v2_markdown_links,
 )


def test_markdown_renderer_includes_operation_sections() -> None:
    spec = {
        "openapi": "3.1.0",
        "info": {"description": "# Intro\n\nWelcome to the demo spec."},
        "servers": [{"url": "https://api.affinity.co"}],
        "tags": [{"name": "demo", "description": "Demo endpoints"}],
        "paths": {
            "/v2/demo": {
                "get": {
                    "summary": "List demos",
                    "operationId": "listDemo",
                    "tags": ["demo"],
                    "parameters": [
                        {
                            "name": "cursor",
                            "in": "query",
                            "schema": {"type": "string"},
                            "description": "Pagination cursor",
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful response",
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/DemoList"},
                                    "examples": {
                                        "success": {
                                            "value": {
                                                "data": [{"id": 1}],
                                            }
                                        }
                                    },
                                }
                            },
                        }
                    },
                }
            }
        },
        "components": {
            "schemas": {
                "DemoList": {
                    "type": "object",
                    "required": ["data"],
                    "properties": {
                        "data": {
                            "type": "array",
                            "items": {"$ref": "#/components/schemas/Demo"},
                        }
                    },
                },
                "Demo": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "description": "Unique identifier"},
                    },
                },
                "Error": {
                    "title": "Error",
                    "oneOf": [{"$ref": "#/components/schemas/Demo"}],
                    "discriminator": {"propertyName": "code", "mapping": {"demo-error": "#/components/schemas/Demo"}},
                },
            }
        },
    }

    ctx = RenderContext(
        source_url="https://developer.affinity.co/",
        fetched_at=datetime(2025, 11, 10, tzinfo=timezone.utc),
        snapshot_path="tmp/v2/developer_affinity_co.html",
        info=spec["info"],
        spec=spec,
    )
    markdown = V2MarkdownRenderer(ctx).build()
    assert "### List demos" in markdown
    assert "`GET /v2/demo`" in markdown
    assert "## Demo" in markdown  # schema reference
    assert "## Error Reference" in markdown


def test_renderer_mentions_every_path_from_spec() -> None:
    spec = {
        "openapi": "3.1.0",
        "info": {"description": "Docs"},
        "servers": [{"url": "https://api.affinity.co"}],
        "paths": {
            "/v2/foo": {
                "get": {
                    "summary": "Get Foo",
                    "operationId": "getFoo",
                    "responses": {"200": {"description": "ok"}},
                }
            },
            "/v2/bar": {
                "get": {
                    "summary": "Get Bar",
                    "operationId": "getBar",
                    "responses": {"200": {"description": "ok"}},
                }
            },
        },
        "components": {"schemas": {}, "responses": {}, "parameters": {}},
    }

    ctx = RenderContext(
        source_url="https://developer.affinity.co/",
        fetched_at=datetime(2025, 11, 10, tzinfo=timezone.utc),
        snapshot_path="tmp/v2/developer_affinity_co.html",
        info=spec["info"],
        spec=spec,
    )
    markdown = V2MarkdownRenderer(ctx).build()
    for path in spec["paths"]:
        assert path in markdown


def test_ref_resolver_handles_recursive_schemas() -> None:
    spec = {
        "components": {
            "schemas": {
                "FilterGroup": {
                    "title": "FilterGroup",
                    "type": "object",
                    "properties": {
                        "filters": {
                            "type": "array",
                            "items": {"oneOf": [{"$ref": "#/components/schemas/FilterGroup"}]},
                        }
                    },
                }
            }
        }
    }
    resolver = RefResolver(spec)
    resolved = resolver.deref({"$ref": "#/components/schemas/FilterGroup"}, track_schema=True)
    assert resolved["title"] == "FilterGroup"
    nested = resolved["properties"]["filters"]["items"]["oneOf"][0]
    assert nested == {"title": "FilterGroup", "x-recursive-ref": "#/components/schemas/FilterGroup"}
    assert resolver.used_schema_names == {"FilterGroup"}

    ctx = RenderContext(
        source_url="https://example.com",
        fetched_at=datetime(2026, 1, 1, tzinfo=timezone.utc),
        snapshot_path="",
        info={},
        spec={"paths": {}, **spec},
    )
    rendered = V2MarkdownRenderer(ctx)._render_schema_properties(resolved, heading_level=4)
    assert "Recursive reference — see [FilterGroup](#filtergroup)" in rendered


def test_write_bytes_if_changed_tracks_diffs(tmp_path: Path) -> None:
    target = tmp_path / "out.bin"
    assert sync_v2_docs.write_bytes_if_changed(target, b"first") is True
    assert sync_v2_docs.write_bytes_if_changed(target, b"first") is False
    assert sync_v2_docs.write_bytes_if_changed(target, b"second") is True


def test_rewrite_v2_markdown_links_rewrites_redoc_fragments_and_broken_urls() -> None:
    markdown = """# Data Model

## Working with Field Data

### Get Foo
`GET /v2/foo`

- **Tag:** demo · **OperationId:** v2_demo_foo__GET · **Stability:** `beta` · **Auth:** bearerAuth

See [Upcoming Changes](#section/Upcoming-Changes).
See [Permissions](#section/Getting-Started/Permissions).
See [Working with Field Data](#section/Data-Model/Working-with-Field-Data).
See [Foo op](#operation/v2_demo_foo__GET).
See [Foo op 2](#tag/demo/operation/v2_demo_foo__GET).
See [interactions.AttendeesPreview](#interactionsattendeespreview).
See [API keys](https://support.affinity.co/hc/en-us/articles/360032633992-How-to-obtain-your-API-Key).
See [permissions](/pages/external-api-v2/permissions) and [mirror](pages/versioning.md).
See [op](/api-reference/demo/get-foo) and [missing op](/api-reference/demo/get-bar).
"""
    rewritten = rewrite_v2_markdown_links(markdown)
    assert "(#upcoming-changes)" in rewritten
    assert "(#permissions)" in rewritten
    assert "(#working-with-field-data)" in rewritten
    assert "(#get-foo)" in rewritten
    assert "https://support.affinity.co/s/article/How-to-Create-and-Manage-API-Keys" in rewritten
    assert "[permissions](https://developer.affinity.co/pages/external-api-v2/permissions)" in rewritten
    assert "[mirror](pages/versioning.md)" in rewritten
    assert "[op](#get-foo)" in rewritten
    assert "[missing op](https://developer.affinity.co/api-reference/demo/get-bar)" in rewritten


SAMPLE_PAGE = """> ## Documentation Index
> Fetch the complete documentation index at: https://developer.affinity.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Versioning

See the [changelog](/pages/changelog/version-migration) and [prior](/pages/changelog/previous-changes.md#top).
Data share is different: [Data Share Versioning](/pages/data-share/versioning.md).
Beta: [Beta Endpoints](/pages/external-api-v2/beta-endpoints.md) and [Affinity](https://www.affinity.co).

```bash theme={null}
curl https://api.affinity.co/v2/auth/whoami
```

***

## Related topics

- [Versioning & Deprecation](/pages/data-share/versioning.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform."""
# Trailing whitespace added in code so editors and pre-commit hooks don't strip it from the fixture.
SAMPLE_PAGE = SAMPLE_PAGE.replace("whoami\n", "whoami   \n")


def test_normalize_page_strips_boilerplate_and_rewrites_links() -> None:
    normalized = site_pages.normalize_page(SAMPLE_PAGE)
    assert normalized.startswith("# Versioning\n")
    assert "Documentation Index" not in normalized
    assert "Related topics" not in normalized
    assert "Mintlify" not in normalized
    assert normalized.rstrip().endswith("```")  # trailing *** rule removed with the footer
    assert "[changelog](version-migration.md)" in normalized
    assert "[prior](previous-changes.md#top)" in normalized
    # Matched on the full path, not the basename.
    assert "(https://developer.affinity.co/pages/data-share/versioning)" in normalized
    assert "(https://developer.affinity.co/pages/external-api-v2/beta-endpoints)" in normalized
    assert "(https://www.affinity.co)" in normalized
    assert "```bash\n" in normalized and "theme=" not in normalized
    assert all(line == line.rstrip() for line in normalized.splitlines())
    assert normalized.endswith("\n") and not normalized.endswith("\n\n")
    assert site_pages.normalize_page(normalized) == normalized


def test_normalize_page_strips_four_line_preamble_variant() -> None:
    page = (
        "> ## Documentation Index\n"
        "> Fetch the documentation index at: https://developer.affinity.co/llms.txt\n"
        "> Full docs: https://developer.affinity.co/llms-full.txt\n"
        "> Use this file to discover all available pages before exploring further.\n\n"
        "# Version Migration\n\nBody.\n"
    )
    assert site_pages.normalize_page(page) == "# Version Migration\n\nBody.\n"


class _FakeResponse:
    def __init__(self, text: str, content_type: str = "text/markdown; charset=utf-8", status: int = 200):
        self.text = text
        self.headers = {"Content-Type": content_type}
        self.status_code = status

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise requests.HTTPError(f"{self.status_code}")


@pytest.mark.parametrize(
    "response",
    [
        _FakeResponse("<!DOCTYPE html><html></html>", content_type="text/html"),
        _FakeResponse("<!DOCTYPE html><html># Versioning</html>"),
        _FakeResponse("# Page not found\n"),
        _FakeResponse("# Versioning\n", status=404),
    ],
)
def test_fetch_page_rejects_error_pages(monkeypatch: pytest.MonkeyPatch, response: _FakeResponse) -> None:
    monkeypatch.setattr(site_pages.requests, "get", lambda *a, **k: response)
    with pytest.raises(site_pages.PageFetchError):
        site_pages.fetch_page(site_pages.PAGES[0])


def test_fetch_page_accepts_markdown(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(site_pages.requests, "get", lambda *a, **k: _FakeResponse(SAMPLE_PAGE))
    assert site_pages.fetch_page(site_pages.PAGES[0]) == SAMPLE_PAGE


INTRO = """# Getting Started

## Error Codes

Errors.

## Versioning

- **2024-01-01** - The current stable version of the v2 API

## Beta Endpoints

Version 2026-09-17 is mentioned here, outside the Versioning section.

# Changelog

## January 30th, 2026

- Something."""


def _renderer(info: dict, pages_link_prefix: str | None = "pages") -> V2MarkdownRenderer:
    spec = {"info": info, "paths": {}, "components": {"schemas": {}}}
    ctx = RenderContext(
        source_url="https://example.com",
        fetched_at=datetime(2026, 1, 1, tzinfo=timezone.utc),
        snapshot_path="",
        info=info,
        spec=spec,
    )
    return V2MarkdownRenderer(ctx, pages_link_prefix=pages_link_prefix)


def test_version_notice_and_stale_section_notes() -> None:
    markdown = _renderer({"description": INTRO, "x-affinity-api-version": "2026-09-17"}).build()
    assert "This copy documents Affinity API v2 version **2026-09-17**" in markdown
    assert "[Versioning](pages/versioning.md)" in markdown
    assert "- **Changelog (mirrored):** [pages/previous-changes.md](pages/previous-changes.md)" in markdown
    # Each note sits directly under its own heading, not at the end of the previous section.
    assert "## Versioning\n\n> **Note (added by this mirror):** The version list below" in markdown
    assert "# Changelog\n\n> **Note (added by this mirror):** This changelog" in markdown
    assert "Errors.\n\n## Versioning" in markdown


def test_versioning_note_omitted_when_embedded_list_is_current() -> None:
    intro = INTRO.replace("2024-01-01** - The current", "2026-09-17** - The current")
    markdown = _renderer({"description": intro, "x-affinity-api-version": "2026-09-17"}).build()
    assert "The version list below" not in markdown
    assert "This changelog is embedded" in markdown


def test_notes_do_not_change_toc_and_fallbacks() -> None:
    info = {"description": INTRO, "x-affinity-api-version": "2026-09-17"}
    with_pages = _renderer(info).build()
    without_pages = _renderer(info, pages_link_prefix=None).build()
    toc = lambda md: md.split("## Table of Contents", 1)[1].split("\n# ", 1)[0]  # noqa: E731
    assert toc(with_pages) == toc(without_pages)
    assert "Note (added by this mirror)" not in without_pages
    assert "pages/" not in without_pages
    no_version = _renderer({"description": "# Intro\n\n## Other\n\nText."}).build()
    assert "This copy documents the current Affinity API v2 version." in no_version


def test_committed_v2_docs_have_no_broken_relative_links() -> None:
    v2_dir = Path(__file__).resolve().parents[1] / "docs" / "v2"
    files = [v2_dir / "affinity_api_docs.md", *sorted((v2_dir / "pages").glob("*.md"))]
    assert len(files) == 1 + len(site_pages.PAGES)
    link_re = re.compile(r"\]\(([^)\s#]+)(?:#[^)\s]*)?\)")
    for md_file in files:
        for target in link_re.findall(md_file.read_text(encoding="utf-8")):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target):
                continue
            assert (md_file.parent / target).exists(), f"{md_file.name}: broken link {target}"


def test_sync_keeps_old_page_and_exits_2_when_a_page_fails(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    spec = {"openapi": "3.1.0", "info": {"x-affinity-api-version": "2026-09-17"}, "paths": {}}
    artifacts = openapi_loader.FetchArtifacts(
        spec=spec,
        fetched_at=datetime(2026, 1, 1, tzinfo=timezone.utc),
        last_modified=None,
        date_header=None,
        source_url="https://example.com/openapi.json",
    )
    monkeypatch.setattr(sync_v2_docs.openapi_loader, "fetch_site", lambda url: artifacts)

    def fake_fetch(page: site_pages.SitePage) -> str:
        if page.output_name == "previous-changes.md":
            raise site_pages.PageFetchError("boom")
        return f"# {page.title}\n\nFresh.\n"

    monkeypatch.setattr(sync_v2_docs.site_pages, "fetch_page", fake_fetch)
    pages_dir = tmp_path / "pages"
    pages_dir.mkdir()
    (pages_dir / "previous-changes.md").write_text("old copy\n")
    argv = [
        "sync_v2_docs.py",
        "--output", str(tmp_path / "doc.md"),
        "--spec-output", str(tmp_path / "openapi.json"),
        "--pages-dir", str(pages_dir),
        "--snapshot-dir", str(tmp_path / "snap"),
    ]
    monkeypatch.setattr(sys, "argv", argv)
    assert sync_v2_docs.main() == sync_v2_docs.PAGES_FAILED_EXIT_CODE
    assert (tmp_path / "doc.md").exists() and (tmp_path / "openapi.json").exists()
    assert (pages_dir / "previous-changes.md").read_text() == "old copy\n"
    assert "Fresh." in (pages_dir / "versioning.md").read_text()

    monkeypatch.setattr(sys, "argv", [*argv, "--fail-on-diff"])
    monkeypatch.setattr(sync_v2_docs.site_pages, "fetch_page", lambda page: f"# {page.title}\n\nChanged.\n")
    with pytest.raises(SystemExit):
        sync_v2_docs.main()
