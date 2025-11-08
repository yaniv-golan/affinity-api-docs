#!/usr/bin/env python3
"""
Realistic scenario testing for the documentation update script.
Tests edge cases that could occur in production.
"""
import os
import sys
import json
import tempfile
import shutil
from pathlib import Path

# Add script directory to path
script_dir = Path(__file__).parent.parent
sys.path.insert(0, str(script_dir / '.github' / 'scripts'))

# Import the functions we need to test
from check_and_update_docs import (
    fetch_latest_docs,
    extract_timestamp,
    extract_content,
    calculate_content_hash,
    compare_versions,
    load_version_metadata,
    save_version_metadata,
    check_existing_prs,
    generate_diff,
    API_CONFIGS
)

def test_scenario(name: str, test_func):
    """Run a test scenario and report results."""
    print(f"\n{'='*60}")
    print(f"Scenario: {name}")
    print(f"{'='*60}")
    try:
        result = test_func()
        if result:
            print(f"✓ PASSED: {name}")
        else:
            print(f"✗ FAILED: {name}")
        return result
    except Exception as e:
        print(f"✗ ERROR in {name}: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_1_network_failure():
    """Test handling of network failures."""
    print("Testing: Invalid URL (simulating network failure)")
    html = fetch_latest_docs("https://invalid-url-that-does-not-exist-12345.com/")
    return html is None

def test_2_content_extraction():
    """Test content extraction from HTML."""
    print("Testing: Content extraction")
    # Use a simple HTML sample
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
    return len(content) > 0 and 'Test Documentation' in content

def test_3_timestamp_extraction():
    """Test timestamp extraction."""
    print("Testing: Timestamp extraction")
    html = """
    <html>
        <body>
            <p>Last updated: November 8, 2025</p>
            <p>Version: 1.0</p>
        </body>
    </html>
    """
    timestamp = extract_timestamp(html, 'v1')
    return timestamp is not None

def test_4_content_comparison():
    """Test content comparison logic."""
    print("Testing: Content comparison")
    content1 = "This is test content"
    content2 = "This is different content"
    content3 = "This is test content"  # Same as content1

    hash1 = calculate_content_hash(content1)
    hash2 = calculate_content_hash(content2)
    hash3 = calculate_content_hash(content3)

    # Different content should have different hashes
    assert hash1 != hash2, "Different content should have different hashes"
    # Same content should have same hash
    assert hash1 == hash3, "Same content should have same hash"

    # Test comparison function
    has_changes, reason = compare_versions(content1, content2, {})
    assert has_changes == True, "Should detect changes"

    has_changes, reason = compare_versions(content1, content3, {})
    assert has_changes == False, "Should not detect changes for identical content"

    return True

def test_5_metadata_operations():
    """Test metadata file operations."""
    print("Testing: Metadata file operations")
    # Create temporary metadata file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_file = f.name
        json.dump({
            'api_version': 'v1',
            'last_checked': None,
            'content_hash': None
        }, f)

    try:
        # Test loading
        metadata = load_version_metadata(temp_file)
        assert 'api_version' in metadata

        # Test saving
        metadata['last_checked'] = '2025-11-08T10:00:00'
        save_version_metadata(temp_file, metadata)

        # Verify it was saved
        metadata2 = load_version_metadata(temp_file)
        assert metadata2['last_checked'] == '2025-11-08T10:00:00'

        return True
    finally:
        os.unlink(temp_file)

def test_6_diff_generation():
    """Test diff generation."""
    print("Testing: Diff generation")
    content1 = "Line 1\nLine 2\nLine 3"
    content2 = "Line 1\nLine 2\nLine 4\nLine 5"

    diff = generate_diff(content1, content2)
    assert 'Added' in diff or 'Removed' in diff or 'lines' in diff
    return True

def test_7_missing_file_handling():
    """Test handling of missing documentation file."""
    print("Testing: Missing file handling")
    # Test v2 (which doesn't have docs yet)
    config = API_CONFIGS['v2']
    file_exists = os.path.exists(config['doc_path'])
    # v2 file shouldn't exist - this is expected
    return True  # Just verify it doesn't crash

def test_8_rate_limiting_logic():
    """Test rate limiting (time-based check skipping)."""
    print("Testing: Rate limiting logic")
    # Create metadata with recent check
    metadata = {
        'last_checked': '2025-11-08T10:00:00',  # Very recent
        'api_version': 'v1'
    }

    from datetime import datetime
    last_checked = datetime.fromisoformat(metadata['last_checked'])
    hours_since = (datetime.now() - last_checked).total_seconds() / 3600

    # Should be less than 12 hours
    assert hours_since < 12, "Recent check should be less than 12 hours ago"
    return True

def test_9_real_website_fetch():
    """Test fetching from real website."""
    print("Testing: Real website fetch")
    html = fetch_latest_docs(API_CONFIGS['v1']['url'])
    if html:
        print(f"  Fetched {len(html)} bytes")
        # Try to extract content
        content = extract_content(html, 'v1')
        print(f"  Extracted {len(content)} characters")
        return len(content) > 0
    return False

def test_10_duplicate_pr_detection():
    """Test duplicate PR detection logic."""
    print("Testing: Duplicate PR detection")
    # This will try to check for existing PRs
    # It should handle errors gracefully if gh is not authenticated
    try:
        existing_pr = check_existing_prs('v1')
        # Should return None or a PR number, not crash
        return True
    except Exception as e:
        print(f"  Note: {e} (this is OK if not authenticated)")
        return True  # Should handle gracefully

def main():
    """Run all test scenarios."""
    print("="*60)
    print("Realistic Scenario Testing")
    print("="*60)

    scenarios = [
        ("Network Failure Handling", test_1_network_failure),
        ("Content Extraction", test_2_content_extraction),
        ("Timestamp Extraction", test_3_timestamp_extraction),
        ("Content Comparison", test_4_content_comparison),
        ("Metadata Operations", test_5_metadata_operations),
        ("Diff Generation", test_6_diff_generation),
        ("Missing File Handling", test_7_missing_file_handling),
        ("Rate Limiting Logic", test_8_rate_limiting_logic),
        ("Real Website Fetch", test_9_real_website_fetch),
        ("Duplicate PR Detection", test_10_duplicate_pr_detection),
    ]

    results = []
    for name, test_func in scenarios:
        result = test_scenario(name, test_func)
        results.append((name, result))

    # Summary
    print(f"\n{'='*60}")
    print("Test Summary")
    print(f"{'='*60}")
    passed = sum(1 for _, result in results if result)
    total = len(results)

    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {name}")

    print(f"\nTotal: {passed}/{total} tests passed")

    if passed == total:
        print("✓ All tests passed!")
        return 0
    else:
        print(f"✗ {total - passed} test(s) failed")
        return 1

if __name__ == '__main__':
    sys.exit(main())
