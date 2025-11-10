# Test Suite

This directory contains tests for the documentation update workflow.

## Test Framework

We use **pytest** for testing, which provides:

- Better test discovery and organization
- Fixtures for test setup/teardown
- Parametrization for testing multiple scenarios
- Better error reporting
- Integration with CI/CD

## Running Tests

### Run All Tests

```bash
pytest tests/
```

### Run with Verbose Output

```bash
pytest tests/ -v
```

### Run Specific Test File

```bash
pytest tests/test_documentation_updates.py
```

### Run Specific Test

```bash
pytest tests/test_documentation_updates.py::TestContentExtraction::test_extract_content_basic
```

### Run Only Unit Tests (Skip Integration)

```bash
pytest tests/ -m "not integration"
```

### Run Only Integration Tests

```bash
pytest tests/ -m integration
```

### Run with Coverage

```bash
pip install pytest-cov
pytest tests/ --cov=tools/v1_sync_pipeline --cov-report=html
```

## Test Organization

- **`test_documentation_updates.py`** - Main pytest test suite
- **`conftest.py`** - Pytest fixtures and configuration
- **`test-local.sh`** - Quick local test script (legacy)
- **`test-edge-cases.sh`** - Edge case smoke tests (legacy helper)
- **`test-production-scenarios.sh`** - Production scenario smoke tests (legacy helper)

## Test Categories

Tests are marked with pytest markers:

- **`@pytest.mark.integration`** - Tests that require network access or external resources
- **`@pytest.mark.unit`** - Fast unit tests with no external dependencies
- **`@pytest.mark.slow`** - Tests that take a long time to run

## Writing New Tests

1. Create test functions starting with `test_`
2. Use descriptive class names starting with `Test`
3. Use fixtures from `conftest.py` for common setup
4. Mark integration tests with `@pytest.mark.integration`
5. Follow pytest best practices

Example:

```python
def test_something(sample_html):
    """Test description."""
    result = extract_content(sample_html, 'v1')
    assert result is not None
```

## CI/CD Integration

Tests run automatically in GitHub Actions. Integration tests are skipped in CI by default to avoid flakiness.

## Legacy Test Scripts

The shell scripts (`test-*.sh`) are kept for backward compatibility but are being phased out in favor of pytest tests.
