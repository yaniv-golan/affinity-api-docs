"""Shared helpers for the v2 sync pipeline."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable
import re


def slugify(title: str) -> str:
    """Generate a GitHub-compatible anchor slug."""
    slug = title.strip().lower()
    slug = slug.replace("/", "-")
    slug = re.sub(r"\s+", "-", slug)
    slug = re.sub(r"[^\w-]", "", slug)
    return slug


def normalize_whitespace(text: str) -> str:
    """Collapse tabs and repeated spaces, remove NBSP."""
    text = text.replace("\xa0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\s+\n", "\n", text)
    return text.strip()


def format_description(text: str) -> str:
    """Normalize description blocks while preserving tables/callouts."""
    if not text:
        return ""
    text = text.replace("\xa0", " ")
    text = text.replace("\r\n", "\n")
    try:
        text = text.encode("latin1", "ignore").decode("utf-8", "ignore")
    except (UnicodeEncodeError, UnicodeDecodeError):
        pass
    lines = [line.rstrip() for line in text.splitlines()]
    text = "\n".join(lines).strip()
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Convert table-styled callouts into blockquotes
    def _callout(match: re.Match[str]) -> str:
        body = match.group(1).strip()
        body = body.lstrip("⚠️").strip()
        return f"> **⚠️ {body}**\n"

    text = re.sub(
        r"\|\s*([^|\n]+?)\s*\|\n\|--\|",
        _callout,
        text,
    )
    # Ensure blank line before markdown tables
    text = re.sub(r"(?<!\|)\n(?=\| )", "\n\n", text)
    # Ensure blank line after table headers ( --- row )
    text = re.sub(r"(\|[-\s]+\|)\n(?!\n)", r"\1\n\n", text)
    # Collapse extra blank lines between table rows
    text = re.sub(r"(?<=\|)\n{2,}(?=\| )", "\n", text)
    return text.strip()


def build_toc(markdown_body: str, max_level: int = 4) -> str:
    """Create a markdown table of contents."""
    toc_lines: list[str] = []
    in_code = False
    slug_counts: dict[str, int] = {}

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
        if level > max_level:
            continue
        title = match.group(2).strip()
        base = slugify(title)
        count = slug_counts.get(base, 0)
        slug_counts[base] = count + 1
        anchor = base if count == 0 else f"{base}-{count}"
        indent = "  " * (level - 1)
        toc_lines.append(f"{indent}- [{title}](#{anchor})")
    return "\n".join(toc_lines)


def format_markdown_list(items: Iterable[str]) -> str:
    """Render iterable of strings as markdown bullet list."""
    return "\n".join(f"- {item}" for item in items)


MOJIBAKE_MAP = {
    "â": "—",
    "â": "'",
    "â": '"',
    "â": '"',
    "â¢": "•",
    "â¦": "…",
}


def fix_mojibake(text: str) -> str:
    """Swap common mojibake sequences with their intended characters."""
    for bad, good in MOJIBAKE_MAP.items():
        text = text.replace(bad, good)
    return text
