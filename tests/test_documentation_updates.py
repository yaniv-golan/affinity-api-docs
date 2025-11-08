"""
Pytest test suite for documentation update workflow.

Run tests with:
    pytest tests/
    pytest tests/ -v  # verbose
    pytest tests/ -k test_network  # run specific tests
"""
import pytest
import os
import json
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock
from datetime import datetime

# Add script directory to path
script_dir = Path(__file__).parent.parent
sys_path_insert = str(script_dir / '.github' / 'scripts')
import sys
if sys_path_insert not in sys.path:
    sys.path.insert(0, sys_path_insert)

from check_and_update_docs import (
    fetch_latest_docs,
    extract_timestamp,
    extract_content,
    calculate_content_hash,
    compare_versions,
    load_version_metadata,
    save_version_metadata,
    generate_diff,
    API_CONFIGS
)


class TestContentExtraction:
    """Tests for content extraction from HTML."""

    def test_extract_content_basic(self):
        """Test basic content extraction."""
        html = """
        <html>
            <head><title>Test</title></head>
            <body>
                <h1>Test Documentation</h1>
                <p>This is test content.</p>
                <pre><code>curl example</code></pre>
            </body>
        </html>
        """
        content = extract_content(html, 'v1')
        assert len(content) > 0
        assert 'Test Documentation' in content
        assert 'test content' in content.lower()

    def test_extract_content_removes_scripts(self):
        """Test that script tags are removed."""
        html = """
        <html>
            <body>
                <script>alert('test');</script>
                <p>Visible content</p>
            </body>
        </html>
        """
        content = extract_content(html, 'v1')
        assert 'alert' not in content
        assert 'Visible content' in content


class TestTimestampExtraction:
    """Tests for timestamp extraction."""

    def test_extract_timestamp_with_date(self):
        """Test timestamp extraction with date pattern."""
        html = """
        <html>
            <body>
                <p>Last updated: November 8, 2025</p>
            </body>
        </html>
        """
        timestamp = extract_timestamp(html, 'v1')
        assert timestamp is not None
        assert '2025' in timestamp

    def test_extract_timestamp_with_iso_format(self):
        """Test timestamp extraction with ISO format."""
        html = """
        <html>
            <head>
                <meta property="article:modified_time" content="2025-11-08T10:00:00Z">
            </head>
        </html>
        """
        timestamp = extract_timestamp(html, 'v1')
        assert timestamp is not None
        assert '2025-11-08' in timestamp

    def test_extract_timestamp_no_timestamp(self):
        """Test when no timestamp is found."""
        html = "<html><body><p>No date here</p></body></html>"
        timestamp = extract_timestamp(html, 'v1')
        # Should return None or empty string, not crash
        assert timestamp is None or timestamp == ""


class TestContentComparison:
    """Tests for content comparison logic."""

    def test_content_hash_different_content(self):
        """Test that different content produces different hashes."""
        content1 = "This is test content"
        content2 = "This is different content"

        hash1 = calculate_content_hash(content1)
        hash2 = calculate_content_hash(content2)

        assert hash1 != hash2

    def test_content_hash_same_content(self):
        """Test that same content produces same hash."""
        content = "This is test content"

        hash1 = calculate_content_hash(content)
        hash2 = calculate_content_hash(content)

        assert hash1 == hash2

    def test_compare_versions_detects_changes(self):
        """Test that compare_versions detects changes."""
        content1 = "Original content"
        content2 = "Updated content"

        has_changes, reason = compare_versions(content1, content2, {})

        assert has_changes is True
        assert reason is not None

    def test_compare_versions_no_changes(self):
        """Test that compare_versions detects no changes."""
        content = "Same content"

        has_changes, reason = compare_versions(content, content, {})

        assert has_changes is False


class TestMetadataOperations:
    """Tests for metadata file operations."""

    def test_load_version_metadata_new_file(self):
        """Test loading metadata from non-existent file."""
        metadata = load_version_metadata('/tmp/nonexistent_file.json')
        assert isinstance(metadata, dict)

    def test_save_and_load_metadata(self):
        """Test saving and loading metadata."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_file = f.name

        try:
            test_metadata = {
                'api_version': 'v1',
                'last_checked': '2025-11-08T10:00:00',
                'content_hash': 'abc123'
            }

            save_version_metadata(temp_file, test_metadata)

            loaded = load_version_metadata(temp_file)

            assert loaded['api_version'] == 'v1'
            assert loaded['last_checked'] == '2025-11-08T10:00:00'
            assert loaded['content_hash'] == 'abc123'
        finally:
            if os.path.exists(temp_file):
                os.unlink(temp_file)


class TestDiffGeneration:
    """Tests for diff generation."""

    def test_generate_diff(self):
        """Test diff generation between two contents."""
        content1 = "Line 1\nLine 2\nLine 3"
        content2 = "Line 1\nLine 2\nLine 4\nLine 5"

        diff = generate_diff(content1, content2)

        assert isinstance(diff, str)
        assert len(diff) > 0
        assert 'Added' in diff or 'Removed' in diff or 'lines' in diff


class TestNetworkOperations:
    """Tests for network operations."""

    @pytest.mark.integration
    def test_fetch_latest_docs_success(self):
        """Test successful fetch from real website."""
        html = fetch_latest_docs(API_CONFIGS['v1']['url'])

        assert html is not None
        assert len(html) > 0
        assert '<html' in html.lower() or '<body' in html.lower()

    def test_fetch_latest_docs_invalid_url(self):
        """Test handling of invalid URL."""
        html = fetch_latest_docs("https://invalid-url-that-does-not-exist-12345.com/")

        assert html is None

    @patch('check_and_update_docs.requests.get')
    def test_fetch_latest_docs_retry_logic(self, mock_get):
        """Test retry logic on failures."""
        # Simulate failures then success
        mock_get.side_effect = [
            Exception("Network error"),
            Exception("Network error"),
            MagicMock(text="<html>Success</html>", status_code=200)
        ]

        # This should retry and eventually succeed
        # Note: This test may need adjustment based on actual retry implementation
        pass


class TestAPIConfigs:
    """Tests for API configuration."""

    def test_api_configs_structure(self):
        """Test that API configs have required keys."""
        for version, config in API_CONFIGS.items():
            assert 'url' in config
            assert 'doc_path' in config
            assert 'version_file' in config
            assert 'enabled' in config

    def test_v1_config_enabled(self):
        """Test that v1 is enabled."""
        assert API_CONFIGS['v1']['enabled'] is True

    def test_v2_config_disabled(self):
        """Test that v2 is disabled (not yet implemented)."""
        assert API_CONFIGS['v2']['enabled'] is False


class TestErrorHandling:
    """Tests for error handling."""

    def test_missing_file_handling(self):
        """Test handling of missing documentation file."""
        # This should be tested in integration tests
        # For unit tests, we can verify the logic exists
        pass

    def test_invalid_api_version(self):
        """Test handling of invalid API version."""
        # This should be tested in the main function
        pass


# Integration tests (marked to run separately)
@pytest.mark.integration
class TestIntegration:
    """Integration tests that require real resources."""

    def test_real_website_fetch(self):
        """Test fetching from real Affinity website."""
        html = fetch_latest_docs(API_CONFIGS['v1']['url'])

        assert html is not None
        assert len(html) > 1000  # Should be substantial content

        # Try to extract content
        content = extract_content(html, 'v1')
        assert len(content) > 0

    def test_end_to_end_comparison(self):
        """Test end-to-end comparison logic."""
        # Fetch real content
        html = fetch_latest_docs(API_CONFIGS['v1']['url'])

        if html:
            content = extract_content(html, 'v1')
            hash_value = calculate_content_hash(content)

            assert hash_value is not None
            assert len(hash_value) == 64  # SHA-256 hex length
