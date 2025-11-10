"""Unit tests for the Affinity v1 documentation sync pipeline."""
from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path
from textwrap import dedent
from types import SimpleNamespace

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.v1_sync_pipeline import sync_v1_docs as sync


def test_normalize_text_replaces_quotes_and_whitespace() -> None:
    raw = "“Smart quotes” — and\xa0non-breaking\tspaces"
    normalized = sync.normalize_text(raw)
    assert '"' in normalized
    assert "--" in normalized  # em dash converted
    assert "\xa0" not in normalized
    assert "  " not in normalized


def test_slugify_removes_special_characters() -> None:
    assert sync.slugify("Deals & Opportunities/2025!") == "deals--opportunities-2025"


def test_build_toc_skips_example_sections() -> None:
    markdown = dedent(
        """
        # Heading One

        ```bash
        echo "not a heading"
        ```

        ## Example Request
        ## Useful Section
        ### Example Response
        """
    ).strip()
    toc = sync.build_toc(markdown)
    assert "[Heading One]" in toc
    assert "Example Request" not in toc
    assert "Useful Section" in toc
    assert "Example Response" not in toc


def test_render_header_includes_timestamp(tmp_path: Path) -> None:
    args = SimpleNamespace(url="https://api-docs.affinity.co/")
    timestamp = datetime(2025, 11, 10, 8, 30, tzinfo=timezone.utc)
    snapshot = tmp_path / "snapshot.html"
    snapshot.write_text("<html></html>")
    toc = "- [Intro](#intro)"

    header = sync.render_header(args, timestamp, snapshot, toc)
    assert "Unofficial" in header or "UNOFFICIAL" in header.upper()
    assert "2025" in header
    assert "Table of Contents" in header


def test_resolve_timestamp_prefers_header_value() -> None:
    fetched = datetime(2025, 11, 10, tzinfo=timezone.utc)
    result = sync.resolve_timestamp("Mon, 10 Nov 2025 12:00:00 GMT", fetched)
    assert result.year == 2025 and result.hour == 12


def test_save_snapshot_creates_file(tmp_path: Path) -> None:
    html = "<html>sample</html>"
    fetched = datetime(2025, 11, 10, 8, 45, tzinfo=timezone.utc)
    snapshot = sync.save_snapshot(html, tmp_path, fetched)
    assert snapshot.exists()
    assert snapshot.read_text() == html


def test_affinity_parser_extracts_text_and_code_samples() -> None:
    html = dedent(
        """
        <html>
          <body>
            <div class="content">
              <h1>Introduction</h1>
              <p>Hello <strong>world</strong></p>
              <pre class="tab-bash"><code>curl https://api.affinity.co/</code></pre>
              <h2 id="people">People</h2>
              <p>Describe the resource.</p>
            </div>
          </body>
        </html>
        """
    )
    parser = sync.AffinityV1Parser(html)
    markdown = parser.build_markdown()
    assert "# Introduction" in markdown
    assert "Hello **world**" in markdown
    assert "curl https://api.affinity.co/" in markdown
    assert parser.code_samples
    assert parser.code_samples[0].language == "bash"
    assert parser.code_samples[0].section == "Introduction"


def test_code_wrapped_anchor_becomes_clickable() -> None:
    html = dedent(
        """
        <html>
          <body>
            <h2 id="get-thing">Heading</h2>
            <div class="content">
              <p><code><a href="#get-thing">GET /thing</a></code></p>
            </div>
          </body>
        </html>
        """
    )
    parser = sync.AffinityV1Parser(html)
    markdown = parser.build_markdown()
    assert "[`GET /thing`](#get-thing)" in markdown
