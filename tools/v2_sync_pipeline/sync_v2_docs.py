#!/usr/bin/env python3
"""Fetch Affinity API v2 docs, render markdown, and save artifacts."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any
import sys
from datetime import datetime

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.v2_sync_pipeline import openapi_loader
from tools.v2_sync_pipeline.markdown_renderer import RenderContext, V2MarkdownRenderer


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sync Affinity API v2 documentation.")
    parser.add_argument("--url", default=openapi_loader.DEFAULT_URL, help="Docs base URL.")
    parser.add_argument(
        "--output",
        default=Path("docs/v2/affinity_api_docs.md"),
        type=Path,
        help="Path to write the generated markdown.",
    )
    parser.add_argument(
        "--spec-output",
        default=Path("docs/v2/openapi.json"),
        type=Path,
        help="Path to write the extracted OpenAPI spec JSON.",
    )
    parser.add_argument(
        "--snapshot-dir",
        default=Path("tmp/v2"),
        type=Path,
        help="Directory for HTML/JSON artifacts.",
    )
    parser.add_argument(
        "--fail-on-diff",
        action="store_true",
        help="Exit with code 1 if generated markdown differs from disk.",
    )
    return parser.parse_args()


def generate_markdown(
    spec: dict[str, Any],
    snapshot_path: Path,
    source_url: str,
    fetched_at: datetime,
) -> str:
    ctx = RenderContext(
        source_url=source_url,
        fetched_at=fetched_at,
        snapshot_path=str(snapshot_path),
        info=spec.get("info", {}),
        spec=spec,
    )
    renderer = V2MarkdownRenderer(ctx)
    return renderer.build()


def write_bytes_if_changed(path: Path, payload: bytes) -> bool:
    previous = path.read_bytes() if path.exists() else None
    content_changed = previous != payload
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)
    return content_changed


def main() -> int:
    args = parse_args()
    artifacts = openapi_loader.fetch_site(args.url)
    spec = artifacts.spec
    saved = openapi_loader.save_artifacts(artifacts, args.snapshot_dir)
    markdown = generate_markdown(
        spec,
        snapshot_path=saved.json_path,
        source_url=args.url,
        fetched_at=artifacts.last_modified or artifacts.date_header or artifacts.fetched_at,
    )
    markdown_payload = (markdown.rstrip() + "\n").encode("utf-8")
    spec_payload = saved.json_path.read_bytes()

    changed_files: list[str] = []
    if write_bytes_if_changed(args.output, markdown_payload):
        changed_files.append(str(args.output))
    if write_bytes_if_changed(args.spec_output, spec_payload):
        changed_files.append(str(args.spec_output))

    if args.fail_on_diff and changed_files:
        changed_list = ", ".join(changed_files)
        raise SystemExit(f"Generated outputs differ from existing output: {changed_list}")

    print(json.dumps({"wrote": [str(args.output), str(args.spec_output)]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
