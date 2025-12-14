"""Tests for the Affinity API v2 sync pipeline."""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from tools.v2_sync_pipeline import openapi_loader
from tools.v2_sync_pipeline import sync_v2_docs
from tools.v2_sync_pipeline.markdown_renderer import (
    RenderContext,
    V2MarkdownRenderer,
    rewrite_v2_markdown_links,
 )


def test_extract_openapi_from_state_handles_json_payload() -> None:
    blob = r"""const __redoc_state = JSON.parse("{\"definition\":{\"data\":{\"info\":{\"title\":\"Demo\"}}}}");"""
    data = openapi_loader.extract_openapi_from_state(blob)
    assert data["info"]["title"] == "Demo"


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
"""
    rewritten = rewrite_v2_markdown_links(markdown)
    assert "(#upcoming-changes)" in rewritten
    assert "(#permissions)" in rewritten
    assert "(#working-with-field-data)" in rewritten
    assert "(#get-foo)" in rewritten
    assert "https://support.affinity.co/s/article/How-to-Create-and-Manage-API-Keys" in rewritten
