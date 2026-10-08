#!/usr/bin/env python3
"""Fetch Affinity API v2 docs, render markdown, and save artifacts."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any
import sys
from datetime import datetime

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.v2_sync_pipeline import openapi_loader, site_pages
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
        "--pages-dir",
        default=Path("docs/v2/pages"),
        type=Path,
        help="Directory for mirrored developer-site pages (versioning, changelogs).",
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
    pages_link_prefix: str | None = None,
) -> str:
    ctx = RenderContext(
        source_url=source_url,
        fetched_at=fetched_at,
        snapshot_path=str(snapshot_path),
        info=spec.get("info", {}),
        spec=spec,
    )
    renderer = V2MarkdownRenderer(ctx, pages_link_prefix=pages_link_prefix)
    return renderer.build()


def write_bytes_if_changed(path: Path, payload: bytes) -> bool:
    previous = path.read_bytes() if path.exists() else None
    content_changed = previous != payload
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)
    return content_changed


PAGES_FAILED_EXIT_CODE = 2


def fetch_site_pages() -> tuple[dict[str, bytes], list[str]]:
    """Fetch and render every mirrored page. Returns (output_name -> payload, failure messages)."""
    payloads: dict[str, bytes] = {}
    failures: list[str] = []
    for page in site_pages.PAGES:
        try:
            raw = site_pages.fetch_page(page)
        except site_pages.PageFetchError as exc:
            failures.append(str(exc))
            continue
        rendered = site_pages.render_page(page, site_pages.normalize_page(raw))
        payloads[page.output_name] = rendered.encode("utf-8")
    return payloads, failures


def _pages_link_prefix(output: Path, pages_dir: Path) -> str:
    return Path(os.path.relpath(pages_dir.resolve(), output.resolve().parent)).as_posix()


def main() -> int:
    args = parse_args()
    artifacts = openapi_loader.fetch_site(args.url)
    spec = artifacts.spec
    # Fetch pages before writing anything; a page failure must not block the spec/doc update.
    page_payloads, page_failures = fetch_site_pages()
    saved = openapi_loader.save_artifacts(artifacts, args.snapshot_dir)
    markdown = generate_markdown(
        spec,
        snapshot_path=saved.json_path,
        source_url=args.url,
        fetched_at=artifacts.last_modified or artifacts.date_header or artifacts.fetched_at,
        pages_link_prefix=_pages_link_prefix(args.output, args.pages_dir),
    )
    markdown_payload = (markdown.rstrip() + "\n").encode("utf-8")
    spec_payload = saved.json_path.read_bytes()

    changed_files: list[str] = []
    if write_bytes_if_changed(args.output, markdown_payload):
        changed_files.append(str(args.output))
    if write_bytes_if_changed(args.spec_output, spec_payload):
        changed_files.append(str(args.spec_output))
    written = [str(args.output), str(args.spec_output)]
    for name, payload in page_payloads.items():
        page_path = args.pages_dir / name
        written.append(str(page_path))
        if write_bytes_if_changed(page_path, payload):
            changed_files.append(str(page_path))

    if args.fail_on_diff and changed_files:
        changed_list = ", ".join(changed_files)
        raise SystemExit(f"Generated outputs differ from existing output: {changed_list}")

    print(json.dumps({"wrote": written}))
    if page_failures:
        # Kept the previous copy of each failed page; fail visibly after writing everything else.
        for message in page_failures:
            print(f"::warning::Could not mirror Affinity site page: {message}")
        return PAGES_FAILED_EXIT_CODE
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
