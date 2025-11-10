#!/usr/bin/env python3
"""Simple anchor checker for the generated Affinity v1 markdown."""
from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import requests


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check anchors + external links in the generated markdown.")
    parser.add_argument(
        "markdown",
        nargs="?",
        default="docs/v1/affinity_api_docs.md",
        help="Markdown file to check (default: docs/v1/affinity_api_docs.md)",
    )
    parser.add_argument("--timeout", type=int, default=10, help="Timeout in seconds for HTTP requests")
    return parser.parse_args()


def slugify(title: str) -> str:
    slug = title.strip().lower()
    slug = slug.replace(" ", "-")
    slug = slug.replace("/", "-")
    slug = re.sub(r"[^\w-]", "", slug)
    return slug


def collect_anchors(lines: Sequence[str]) -> Iterable[str]:
    slug_counts: Dict[str, int] = {}
    for line in lines:
        match = re.match(r"^(#+)\s+(.*)", line)
        if not match:
            continue
        title = match.group(2).strip()
        base = slugify(title)
        count = slug_counts.get(base, 0)
        slug_counts[base] = count + 1
        anchor = base if count == 0 else f"{base}-{count}"
        yield anchor


def analyze_links(text: str, anchor_set: set[str], timeout: int) -> Tuple[List[Tuple[str, str]], Dict[str, str | int]]:
    link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
    links = link_pattern.findall(text)
    internal_missing: List[Tuple[str, str]] = []
    external_status: Dict[str, str | int] = {}

    for label, url in links:
        if url.startswith("mailto:"):
            continue
        if url.startswith("#"):
            target = url[1:]
            if target and target not in anchor_set:
                internal_missing.append((label, url))
            continue
        if not url.startswith(("http://", "https://")):
            continue
        if url in external_status:
            continue
        try:
            resp = requests.head(url, timeout=timeout, allow_redirects=True)
            status_code = resp.status_code
            if status_code >= 400:
                resp = requests.get(url, timeout=timeout)
                status_code = resp.status_code
            external_status[url] = status_code
        except Exception as exc:  # pragma: no cover - network variability
            external_status[url] = str(exc)

    return internal_missing, external_status


def main() -> None:
    args = parse_args()
    md_path = Path(args.markdown)
    if not md_path.exists():
        raise SystemExit(f"Markdown file not found: {md_path}")

    text = md_path.read_text()
    anchors = set(collect_anchors(text.splitlines()))
    internal_missing, external_status = analyze_links(text, anchors, args.timeout)

    print(f"Internal anchor issues: {len(internal_missing)}")
    for label, url in internal_missing:
        print(f"  missing anchor for [{label}]({url})")

    print("\nExternal link statuses:")
    for url, status in sorted(external_status.items()):
        print(f"  {status}: {url}")


if __name__ == "__main__":
    main()
