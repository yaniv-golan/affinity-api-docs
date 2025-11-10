#!/usr/bin/env python3
"""Fetch Affinity API v2 docs, render markdown, and save artifacts."""
from __future__ import annotations

import argparse
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


def main() -> int:
    args = parse_args()
    artifacts = openapi_loader.fetch_site(args.url)
    spec = openapi_loader.extract_openapi_from_state(artifacts.state_js)
    saved = openapi_loader.save_artifacts(artifacts, spec, args.snapshot_dir)
    markdown = generate_markdown(
        spec,
        snapshot_path=saved.html_path,
        source_url=args.url,
        fetched_at=artifacts.last_modified or artifacts.date_header or artifacts.fetched_at,
    )
    output_text = markdown.rstrip() + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    previous = args.output.read_text(encoding="utf-8") if args.output.exists() else None
    content_changed = previous != output_text
    args.output.write_text(output_text, encoding="utf-8")
    if args.fail_on_diff and content_changed:
        raise SystemExit("Generated documentation differs from existing output")
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
