"""
Pytest configuration and fixtures.
"""
import pytest
import os
import tempfile
import json
from pathlib import Path


@pytest.fixture
def temp_metadata_file():
    """Create a temporary metadata file for testing."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump({
            'api_version': 'v1',
            'last_checked': None,
            'content_hash': None,
            'pr_number': None
        }, f)
        temp_file = f.name

    yield temp_file

    # Cleanup
    if os.path.exists(temp_file):
        os.unlink(temp_file)


@pytest.fixture
def sample_html():
    """Sample HTML for testing."""
    return """
    <html>
        <head>
            <title>Test Documentation</title>
            <meta property="article:modified_time" content="2025-11-08T10:00:00Z">
        </head>
        <body>
            <h1>Test Documentation</h1>
            <p>Last updated: November 8, 2025</p>
            <pre><code>curl -X GET https://api.example.com/endpoint</code></pre>
            <p>This is test content.</p>
        </body>
    </html>
    """


@pytest.fixture
def sample_markdown():
    """Sample markdown content for testing."""
    return """# Test Documentation

This is test markdown content.

## Section 1

Some content here.
"""


@pytest.fixture(autouse=True)
def reset_environment(monkeypatch):
    """Reset environment variables before each test."""
    # Add any environment variable resets here if needed
    pass
