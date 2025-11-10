#!/usr/bin/env python3
"""Systematic comparison of generated markdown vs live browser content."""
from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import List, Tuple


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compare generated markdown to a captured browser snapshot.")
    parser.add_argument(
        "--markdown",
        default="docs/v1/affinity_api_docs.md",
        help="Path to the generated markdown file (default: docs/v1/affinity_api_docs.md)",
    )
    parser.add_argument(
        "--snapshot",
        default="tmp/current_live_site.html",
        help="Path to the saved browser snapshot (default: tmp/current_live_site.html)",
    )
    return parser.parse_args()

def extract_browser_text_sections(snapshot_file: Path) -> dict[str, str]:
    """Extract text from browser snapshot by section."""
    content = snapshot_file.read_text()
    lines = content.split('\n')

    sections = {}
    current_heading = None
    current_text = []

    for line in lines:
        # Look for headings
        if 'heading' in line and '[level=' in line:
            # Save previous section
            if current_heading:
                sections[current_heading] = '\n'.join(current_text)

            # Extract heading text
            match = re.search(r'heading "([^"]+)"', line)
            if match:
                current_heading = match.group(1)
                current_text = []

        # Extract text content
        elif 'text:' in line:
            match = re.search(r'text:\s*(.+)', line)
            if match:
                text = match.group(1).strip()
                if text and current_heading:
                    current_text.append(text)

    # Save last section
    if current_heading:
        sections[current_heading] = '\n'.join(current_text)

    return sections

def extract_markdown_sections(md_file: Path) -> dict[str, str]:
    """Extract sections from markdown file."""
    content = md_file.read_text()
    lines = content.split('\n')

    sections = {}
    current_heading = None
    current_text = []

    for line in lines:
        # Look for markdown headings
        if line.startswith('#'):
            # Save previous section
            if current_heading:
                sections[current_heading] = '\n'.join(current_text)

            # Extract heading
            current_heading = line.lstrip('#').strip()
            current_text = []
        elif line.strip() and current_heading:
            # Skip code blocks and tables for now
            if not line.startswith('```') and not line.startswith('|'):
                current_text.append(line.strip())

    # Save last section
    if current_heading:
        sections[current_heading] = '\n'.join(current_text)

    return sections

def compare_sections(browser_sections: dict, md_sections: dict) -> List[Tuple[str, str]]:
    """Compare sections and find differences."""
    issues = []

    # Check for missing sections
    browser_headings = set(browser_sections.keys())
    md_headings = set(md_sections.keys())

    missing_in_md = browser_headings - md_headings
    extra_in_md = md_headings - browser_headings

    if missing_in_md:
        for heading in sorted(missing_in_md):
            issues.append(('MISSING_SECTION', f"Section '{heading}' exists in browser but missing in markdown"))

    if extra_in_md:
        for heading in sorted(extra_in_md):
            # Skip TOC and disclaimer sections
            if heading not in ['Table of Contents', 'About This Document', 'Contact & Support']:
                issues.append(('EXTRA_SECTION', f"Section '{heading}' exists in markdown but not in browser"))

    # Compare common sections
    common = browser_headings & md_headings
    for heading in sorted(common):
        browser_text = browser_sections[heading].replace('\n', ' ')
        md_text = md_sections[heading].replace('\n', ' ')

        # Basic text comparison (normalize whitespace)
        browser_text_norm = ' '.join(browser_text.split())
        md_text_norm = ' '.join(md_text.split())

        if browser_text_norm and md_text_norm:
            # Check if texts are significantly different (>20% difference)
            longer = max(len(browser_text_norm), len(md_text_norm))
            if longer > 0:
                similarity = len(set(browser_text_norm.split()) & set(md_text_norm.split())) / len(set(browser_text_norm.split()) | set(md_text_norm.split()))
                if similarity < 0.7:
                    issues.append(('TEXT_DIFF', f"Section '{heading}' has significant text differences (similarity: {similarity:.1%})"))

    return issues

def main() -> None:
    args = parse_args()
    print("=" * 80)
    print("SYSTEMATIC COMPARISON: Generated Markdown vs Live Browser")
    print("=" * 80)
    print()

    # Load files
    md_file = Path(args.markdown)
    snapshot_file = Path(args.snapshot)

    if not md_file.exists():
        print(f"ERROR: Markdown file not found: {md_file}")
        return

    if not snapshot_file.exists():
        print(f"ERROR: Browser snapshot not found: {snapshot_file}")
        return

    print(f"Markdown file: {md_file} ({md_file.stat().st_size:,} bytes)")
    print(f"Browser snapshot: {snapshot_file} ({snapshot_file.stat().st_size:,} bytes)")
    print()

    # Extract sections
    print("Extracting sections from browser snapshot...")
    browser_sections = extract_browser_text_sections(snapshot_file)
    print(f"  Found {len(browser_sections)} sections")

    print("Extracting sections from markdown...")
    md_sections = extract_markdown_sections(md_file)
    print(f"  Found {len(md_sections)} sections")
    print()

    # Compare
    print("Comparing sections...")
    issues = compare_sections(browser_sections, md_sections)
    print()

    if issues:
        print("=" * 80)
        print(f"FOUND {len(issues)} ISSUES")
        print("=" * 80)
        print()

        # Group by type
        by_type = {}
        for issue_type, message in issues:
            if issue_type not in by_type:
                by_type[issue_type] = []
            by_type[issue_type].append(message)

        for issue_type, messages in sorted(by_type.items()):
            print(f"\n{issue_type}:")
            for i, msg in enumerate(messages, 1):
                print(f"  {i}. {msg}")
    else:
        print("✓ No major issues found")
        print("  Sections match between browser and markdown")

    # Show some sample sections for manual review
    print()
    print("=" * 80)
    print("SAMPLE SECTION COMPARISON")
    print("=" * 80)

    sample_headings = ['Introduction', 'Authentication', 'The List Resource']
    for heading in sample_headings:
        if heading in browser_sections and heading in md_sections:
            print(f"\n### {heading}")
            print(f"Browser ({len(browser_sections[heading])} chars):")
            print(f"  {browser_sections[heading][:150]}...")
            print(f"Markdown ({len(md_sections[heading])} chars):")
            print(f"  {md_sections[heading][:150]}...")

if __name__ == "__main__":
    main()
