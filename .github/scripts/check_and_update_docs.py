#!/usr/bin/env python3
"""
Check for updates to Affinity API documentation and create PRs if updates are detected.

This script:
1. Fetches the latest documentation from the Affinity website
2. Compares it with the current version in the repository
3. Creates a PR with updated documentation if changes are detected
4. Adds a notice section to the documentation about the update
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup

# Configuration for each API version
API_CONFIGS = {
    "v1": {
        "url": "https://api-docs.affinity.co/",
        "doc_path": "docs/v1/affinity_api_docs.md",
        "version_file": ".github/docs-version-v1.json",
        "enabled": True,
    },
    "v2": {
        "url": "https://developer.affinity.co/",
        "doc_path": "docs/v2/affinity_api_docs.md",
        "version_file": ".github/docs-version-v2.json",
        "enabled": False,  # Not yet implemented
    },
}

# Notice template - NO LONGER USED
# The script no longer modifies the markdown file automatically.
# Instead, it creates an alert PR with reference files for manual review.
NOTICE_TEMPLATE = None  # Deprecated


def fetch_latest_docs(
    url: str, max_retries: int = 3, retry_delay: int = 5
) -> str | None:
    """
    Fetch HTML content from the Affinity website with retries and error handling.

    Args:
        url: URL to fetch
        max_retries: Maximum number of retry attempts
        retry_delay: Delay between retries in seconds

    Returns:
        HTML content as string, or None if fetch failed
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Affinity-Docs-Updater/1.0; +https://github.com)"
    }

    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                wait_time = retry_delay * (2**attempt)  # Exponential backoff
                print(
                    f"Error fetching {url} (attempt {attempt + 1}/{max_retries}): {e}"
                )
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print(f"Failed to fetch {url} after {max_retries} attempts: {e}")
                return None

    return None


def extract_timestamp(html: str, api_version: str) -> str | None:
    """
    Extract "last updated" timestamp from the HTML.

    Args:
        html: HTML content
        api_version: API version (v1 or v2)

    Returns:
        Timestamp string if found, None otherwise
    """
    soup = BeautifulSoup(html, "lxml")

    # Try to find timestamp in various common locations
    # Look for text containing "last updated", "updated", etc.
    patterns = [
        r"last\s+updated[:\s]+([^<\n]+)",
        r"updated[:\s]+([^<\n]+)",
        r"version[:\s]+([^<\n]+)",
    ]

    text_content = soup.get_text().lower()
    for pattern in patterns:
        match = re.search(pattern, text_content, re.IGNORECASE)
        if match:
            return match.group(1).strip()

    # Try to find in meta tags
    meta_date = soup.find("meta", {"property": "article:modified_time"})
    if meta_date and meta_date.get("content"):
        return meta_date.get("content")

    # Try to find in any date-like format
    date_patterns = [
        r"\d{4}-\d{2}-\d{2}",
        r"\d{1,2}/\d{1,2}/\d{4}",
        r"\w+\s+\d{1,2},?\s+\d{4}",
    ]

    for pattern in date_patterns:
        matches = re.findall(pattern, text_content)
        if matches:
            return matches[-1]  # Return the last (most recent) date found

    return None


def extract_content(html: str, api_version: str) -> str:
    """
    Extract raw HTML content for change detection only.

    NOTE: This function does NOT convert HTML to markdown. It returns the raw HTML
    for hash comparison to detect when the source documentation has changed.
    The actual markdown documentation must be updated manually by comparing the
    live site with the current markdown and making careful, surgical edits.

    Args:
        html: HTML content
        api_version: API version (v1 or v2)

    Returns:
        Raw HTML content (NOT markdown)
    """
    soup = BeautifulSoup(html, "lxml")

    # Remove script and style elements for cleaner comparison
    for script in soup(["script", "style", "nav", "header", "footer"]):
        script.decompose()

    # Find the main content area (adjust selector based on site structure)
    main_content = soup.find("main") or soup.find("article") or soup.find("body")

    if main_content:
        return str(main_content)

    return html


def calculate_content_hash(content: str) -> str:
    """Calculate SHA-256 hash of content."""
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def load_version_metadata(version_file: str) -> dict:
    """Load version metadata from JSON file."""
    if os.path.exists(version_file):
        try:
            with open(version_file) as f:
                return json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            print(f"Error loading version metadata from {version_file}: {e}")
            return {}
    return {}


def save_version_metadata(version_file: str, metadata: dict) -> None:
    """Save version metadata to JSON file."""
    os.makedirs(os.path.dirname(version_file), exist_ok=True)
    with open(version_file, "w") as f:
        json.dump(metadata, f, indent=2)


def compare_versions(
    current_content: str, latest_content: str, version_metadata: dict
) -> tuple[bool, str | None]:
    """
    Compare current and latest versions.

    Returns:
        Tuple of (has_changes: bool, reason: str or None)
    """
    current_hash = calculate_content_hash(current_content)
    latest_hash = calculate_content_hash(latest_content)

    # Check if content hash changed
    if current_hash != latest_hash:
        return True, "Content hash changed"

    # Check if timestamp changed (if we have timestamps)
    if version_metadata.get("last_known_timestamp"):
        # This would require extracting timestamp from latest_content
        # For now, we rely on content hash
        pass

    return False, None


def check_existing_prs(api_version: str) -> int | None:
    """
    Check if a PR already exists for this API version.

    Returns:
        PR number if found, None otherwise
    """
    try:
        # Use GitHub CLI to search for open PRs
        branch_pattern = f"docs/auto-update-{api_version}-"
        result = subprocess.run(
            ["gh", "pr", "list", "--state", "open", "--json", "number,headRefName"],
            capture_output=True,
            text=True,
            check=False,
        )

        if result.returncode == 0:
            prs = json.loads(result.stdout)
            for pr in prs:
                if pr["headRefName"].startswith(branch_pattern):
                    return pr["number"]
    except (
        subprocess.CalledProcessError,
        json.JSONDecodeError,
        FileNotFoundError,
    ) as e:
        print(f"Error checking for existing PRs: {e}")

    return None


def generate_diff(current_content: str, latest_content: str) -> str:
    """Generate a diff between current and latest content."""
    # Simple line-by-line diff summary
    current_lines = current_content.splitlines()
    latest_lines = latest_content.splitlines()

    added = len(set(latest_lines) - set(current_lines))
    removed = len(set(current_lines) - set(latest_lines))

    return f"Added: ~{added} lines, Removed: ~{removed} lines"


def update_doc_header(doc_content: str, api_version: str, update_timestamp: str) -> str:
    """
    DEPRECATED: No longer used - we don't automatically modify the markdown.

    Update the documentation header with the latest timestamp.

    Args:
        doc_content: Current documentation content
        api_version: API version (v1 or v2)
        update_timestamp: Timestamp string to insert

    Returns:
        Updated documentation content
    """
    # Format timestamp for display
    try:
        dt = datetime.fromisoformat(update_timestamp.replace("Z", "+00:00"))
        formatted_date = dt.strftime("%B %d, %Y at %H:%M:%S")
        formatted_date_short = dt.strftime("%m/%d/%Y %H:%M:%S")
    except (ValueError, AttributeError):
        # Fallback if timestamp parsing fails
        formatted_date = update_timestamp
        formatted_date_short = update_timestamp

    # Update the "Documentation Version" line
    # Pattern: **Documentation Version:** ... (Last updated: ...)
    # Try to match the existing format first
    version_pattern = r"(\*\*Documentation Version:\*\*.*?\(Last updated:)[^)]+\)"
    replacement = f"\\1 {formatted_date_short}). This copy is automatically synchronized with the official documentation via GitHub Actions."

    updated_content = re.sub(version_pattern, replacement, doc_content, flags=re.DOTALL)

    # If pattern didn't match, try a more flexible pattern
    if updated_content == doc_content:
        version_pattern_flexible = r"(\*\*Documentation Version:\*\*.*?appeared on \*\*)[^*]+(\*\*.*?\(Last updated:)[^)]+\)"
        replacement_flexible = f"\\1{formatted_date}\\2 {formatted_date_short}). This copy is automatically synchronized with the official documentation via GitHub Actions."
        updated_content = re.sub(
            version_pattern_flexible, replacement_flexible, doc_content, flags=re.DOTALL
        )

    # If still no match, try to insert/update at end of line
    if updated_content == doc_content and "Documentation Version:" in doc_content:
        # Find the line and update it
        lines = updated_content.split("\n")
        for i, line in enumerate(lines):
            if "Documentation Version:" in line and "Last updated:" in line:
                lines[
                    i
                ] = f"**Documentation Version:** This copy is based on the official documentation as it appeared on **{formatted_date}** (Last updated: {formatted_date_short}). This copy is automatically synchronized with the official documentation via GitHub Actions."
                updated_content = "\n".join(lines)
                break

    # Also update the "Source:" line to mention automated updates
    source_pattern = r"\*\*Source:\*\*.*?https://[^\s]+"
    source_replacement = f"**Source:** Extracted from the live Affinity API documentation at {API_CONFIGS[api_version]['url']} (automatically updated via GitHub Actions)"

    updated_content = re.sub(source_pattern, source_replacement, updated_content)

    return updated_content


def update_docs_with_notice(
    doc_path: str,
    api_version: str,
    pr_url: str,
    update_date: str,
    pr_number: int,
    pr_title: str,
    source_url: str,
) -> None:
    """
    DEPRECATED: No longer used - we don't automatically modify the markdown.

    Add notice section to documentation file.

    Inserts the notice after the disclaimer section at the top.
    """
    if not os.path.exists(doc_path):
        print(f"Warning: Documentation file {doc_path} does not exist")
        return

    with open(doc_path) as f:
        content = f.read()

    # Find insertion point (after the disclaimer section)
    # Look for the "---" separator after the disclaimer
    notice = NOTICE_TEMPLATE.format(
        update_date=update_date,
        pr_number=pr_number,
        pr_url=pr_url,
        pr_title=pr_title,
        source_url=source_url,
    )

    # Check if notice already exists (to avoid duplicates)
    if f"PR #{pr_number}" in content:
        print(f"Notice for PR #{pr_number} already exists in {doc_path}")
        return

    # Insert after the first "---" separator (after disclaimer)
    separator_pattern = r"(^---\s*$)"
    match = re.search(separator_pattern, content, re.MULTILINE)

    if match:
        insert_pos = match.end()
        new_content = content[:insert_pos] + "\n" + notice + "\n" + content[insert_pos:]
    else:
        # If no separator found, insert after the first heading
        new_content = (
            content.split("\n", 1)[0]
            + "\n\n"
            + notice
            + "\n\n"
            + content.split("\n", 1)[1]
        )

    with open(doc_path, "w") as f:
        f.write(new_content)


def create_pr(
    api_version: str, branch_name: str, pr_title: str, pr_body: str
) -> dict | None:
    """
    Create a PR using GitHub CLI.

    Returns:
        PR data dict if successful, None otherwise
    """
    try:
        # Create the PR
        result = subprocess.run(
            [
                "gh",
                "pr",
                "create",
                "--title",
                pr_title,
                "--body",
                pr_body,
                "--head",
                branch_name,
                "--base",
                "main",
                "--label",
                "auto-update,documentation",
                "--json",
                "number,url,title",
            ],
            capture_output=True,
            text=True,
            check=True,
        )

        pr_data = json.loads(result.stdout)
        print(f"Created PR #{pr_data['number']}: {pr_data['url']}")
        return pr_data

    except subprocess.CalledProcessError as e:
        print(f"Error creating PR: {e}")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing PR response: {e}")
        return None


def check_and_update_docs(
    api_version: str, force_check: bool = False, dry_run: bool = False
) -> bool:
    """
    Main function to check and update documentation for a specific API version.

    Returns:
        True if update was detected and PR created, False otherwise
    """
    if api_version not in API_CONFIGS:
        print(f"Error: Unknown API version '{api_version}'")
        return False

    config = API_CONFIGS[api_version]

    if not config["enabled"]:
        print(f"Skipping {api_version} - not yet enabled")
        return False

    print(f"\n{'=' * 60}")
    print(f"Checking {api_version.upper()} documentation")
    print(f"{'=' * 60}")

    # Load version metadata
    version_metadata = load_version_metadata(config["version_file"])

    # Check if we should skip (unless forced)
    if not force_check and version_metadata.get("last_checked"):
        last_checked = datetime.fromisoformat(version_metadata["last_checked"])
        hours_since_check = (datetime.now() - last_checked).total_seconds() / 3600
        if hours_since_check < 12:  # Don't check more than twice per day
            print(f"Skipping {api_version} - checked {hours_since_check:.1f} hours ago")
            return False

    # Fetch latest documentation
    print(f"Fetching latest documentation from {config['url']}...")
    html = fetch_latest_docs(config["url"])

    if not html:
        print(f"Failed to fetch {api_version} documentation")
        return False

    # Extract content and timestamp
    latest_content = extract_content(html, api_version)
    timestamp = extract_timestamp(html, api_version)

    # Load current documentation
    if not os.path.exists(config["doc_path"]):
        print(
            f"Warning: Current documentation file {config['doc_path']} does not exist"
        )
        # For v2, this is expected - skip for now
        if api_version == "v2":
            print(f"Skipping {api_version} - documentation not yet implemented")
            return False

    with open(config["doc_path"]) as f:
        current_content = f.read()

    # Compare versions
    has_changes, reason = compare_versions(
        current_content, latest_content, version_metadata
    )

    if not has_changes:
        print(f"No changes detected for {api_version}")
        # Update last_checked timestamp
        version_metadata["last_checked"] = datetime.now().isoformat()
        save_version_metadata(config["version_file"], version_metadata)
        return False

    print(f"Changes detected for {api_version}: {reason}")

    # Check for existing PR
    existing_pr = check_existing_prs(api_version)
    if existing_pr:
        print(f"PR already exists for {api_version}: #{existing_pr}")
        # Update metadata with existing PR number
        version_metadata["pr_number"] = existing_pr
        version_metadata["last_checked"] = datetime.now().isoformat()
        save_version_metadata(config["version_file"], version_metadata)
        return False

    # Generate diff summary
    diff_summary = generate_diff(current_content, latest_content)

    # Create branch and commit changes
    timestamp_str = datetime.now().strftime("%Y-%m-%d")
    content_hash_short = calculate_content_hash(latest_content)[:8]
    branch_name = f"docs/auto-update-{api_version}-{timestamp_str}-{content_hash_short}"

    if dry_run:
        print(f"[DRY RUN] Would create branch: {branch_name}")
        print(f"[DRY RUN] Diff summary: {diff_summary}")
        print(
            f"[DRY RUN] Would create PR with title: Auto-update: Affinity API {api_version.upper()} docs updated on {timestamp_str}"
        )
        # Update last_checked timestamp even in dry run
        version_metadata["last_checked"] = datetime.now().isoformat()
        save_version_metadata(config["version_file"], version_metadata)
        return True

    print(f"Creating branch: {branch_name}")

    try:
        # Ensure we're on main branch first
        subprocess.run(["git", "checkout", "main"], check=True)
        # Create and checkout branch
        subprocess.run(["git", "checkout", "-b", branch_name], check=True)

        # Save the raw HTML for manual comparison (don't touch the markdown!)
        html_path = config["doc_path"].replace(".md", "_live_snapshot.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(latest_content)

        # Create a summary file explaining what changed
        summary_path = config["doc_path"].replace(".md", "_update_summary.txt")
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write("Documentation Update Detected\n")
            f.write(f"{'=' * 60}\n\n")
            f.write(f"Source: {config['url']}\n")
            f.write(f"Detected: {datetime.now().isoformat()}\n")
            f.write(f"Timestamp from source: {timestamp or 'Not found'}\n\n")
            f.write("What Changed:\n")
            f.write(f"{diff_summary}\n\n")
            f.write("Manual Review Required:\n")
            f.write(f"{'=' * 60}\n")
            f.write(f"The live documentation at {config['url']} has changed.\n")
            f.write(
                "Please manually compare the live site with the current markdown:\n"
            )
            f.write(f"  1. View live site: {config['url']}\n")
            f.write(f"  2. Compare with: {config['doc_path']}\n")
            f.write("  3. Make careful, surgical edits to fix any discrepancies\n")
            f.write("  4. Test the updated markdown\n")
            f.write("  5. Delete this update branch after merging changes to main\n\n")
            f.write(f"Raw HTML snapshot saved to: {html_path}\n")
            f.write(
                "(For reference only - do NOT use automated HTML-to-markdown conversion)\n"
            )

        # Stage both files
        subprocess.run(["git", "add", html_path, summary_path], check=True)

        # Commit
        commit_message = f"Alert: {api_version.upper()} docs changed on live site ({timestamp_str})\n\nManual review and update required.\n\n{diff_summary}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Push branch
        subprocess.run(["git", "push", "-u", "origin", branch_name], check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error creating branch/commit: {e}")
        return False

    # Create PR
    pr_title = f"Alert: {api_version.upper()} docs changed on live site - Manual review required"
    pr_body = f"""## 🔔 Documentation Change Detected

The live documentation at [{config["url"]}]({config["url"]}) has changed.

**Source**: [{api_version.upper()} API Documentation]({config["url"]})
**Detected**: {datetime.now().strftime("%Y-%m-%d %H:%M UTC")}
**Source Timestamp**: {timestamp or "Not found"}

---

## ⚠️ Manual Review Required

This PR does **NOT** contain automatic updates to the markdown file.

**Why?** Automated HTML-to-markdown conversion destroys document structure and creates malformed content. Instead, this PR contains:

1. **HTML Snapshot** (`{html_path.split('/')[-1]}`): Raw HTML from the live site for reference
2. **Update Summary** (`{summary_path.split('/')[-1]}`): Description of what changed

---

## 📋 Action Items

To update the documentation:

1. **Compare**: Open [{config["url"]}]({config["url"]}) and `{config["doc_path"]}`
2. **Identify**: Find the specific sections that changed
3. **Edit**: Make careful, surgical edits to the markdown file
4. **Validate**: Check formatting, code examples, and structure
5. **Test**: Ensure markdown renders correctly
6. **Commit**: Push changes to `main` branch (NOT this branch)
7. **Close**: Close this PR after manual update is complete

---

## 📊 Detected Changes

{diff_summary}

---

## ℹ️ About This Alert

This automated alert is triggered when the content hash of the live documentation changes. It serves as a notification that the source documentation has been updated and the markdown file may need corresponding updates.

**Do NOT merge this PR** - it only contains reference files, not the actual markdown updates."""

    pr_data = create_pr(api_version, branch_name, pr_title, pr_body)

    if not pr_data:
        print(f"Failed to create PR for {api_version}")
        return False

    # Do NOT modify the markdown file - manual review required
    print(f"✅ Alert PR created: #{pr_data['number']}")
    print("📝 Manual review required - see PR for details")

    # Update version metadata
    version_metadata.update(
        {
            "last_checked": datetime.now().isoformat(),
            "last_known_timestamp": timestamp,
            "content_hash": calculate_content_hash(latest_content),
            "pr_number": pr_data["number"],
            "last_successful_update": datetime.now().isoformat(),
        }
    )
    save_version_metadata(config["version_file"], version_metadata)

    print(f"Successfully created PR #{pr_data['number']} for {api_version}")
    return True


def main():
    """Main entry point."""
    # Ensure we're in the repository root
    script_dir = Path(__file__).parent.parent.parent
    os.chdir(script_dir)

    parser = argparse.ArgumentParser(
        description="Check for Affinity API documentation updates"
    )
    parser.add_argument(
        "--api-version",
        choices=["v1", "v2", "all"],
        default="all",
        help="API version to check (default: all)",
    )
    parser.add_argument(
        "--force-check",
        type=str,
        default="false",
        help="Force check even if recently checked (default: false)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Dry run mode: check for updates but do not create PRs or commits",
    )

    args = parser.parse_args()

    force_check = args.force_check.lower() in ("true", "1", "yes")
    dry_run = args.dry_run

    if dry_run:
        print("=" * 60)
        print("DRY RUN MODE - No PRs or commits will be created")
        print("=" * 60)

    versions_to_check = (
        ["v1", "v2"] if args.api_version == "all" else [args.api_version]
    )

    results = {}
    for version in versions_to_check:
        try:
            results[version] = check_and_update_docs(version, force_check, dry_run)
        except Exception as e:
            print(f"Error processing {version}: {e}")
            import traceback

            traceback.print_exc()
            results[version] = False

    # Summary
    print(f"\n{'=' * 60}")
    print("Summary")
    print(f"{'=' * 60}")
    for version, updated in results.items():
        status = "Updated" if updated else "No changes"
        print(f"{version.upper()}: {status}")

    # Exit with error if any critical failures occurred
    # (but don't fail if just "no changes")
    sys.exit(0)


if __name__ == "__main__":
    main()
