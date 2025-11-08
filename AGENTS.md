# AGENTS.md

## Project Overview

This repository contains extracted and cleaned API documentation for **both Affinity API v1 and v2**. Both versions will be maintained in this repository.

**Affinity API Versions:**
- **v1**: Legacy API documented at https://api-docs.affinity.co/
  - Currently being worked on - main file: `docs/v1/affinity_api_docs.md`
- **v2**: New API with different approach/terminology, documented at https://developer.affinity.co/
  - Planned for future work - folder ready at `docs/v2/`
  - v2 is **not** a superset of v1 - they are separate APIs with different designs

The current v1 documentation file is located at `docs/v1/affinity_api_docs.md` and contains:
- Complete API endpoint documentation
- Request/response formats
- Parameter descriptions
- Resource schemas
- Rate limiting information
- Common use cases
- Changelog

## Current Status

The markdown file has been:
- ✅ Extracted from the live documentation site
- ✅ Fixed encoding issues and typos
- ✅ Corrected formatting inconsistencies
- ✅ Standardized markdown syntax
- ✅ Fixed table formatting
- ✅ Corrected outline/TOC structure
- ⚠️ **Missing**: Code examples (cURL, Ruby, Python, Node.js) for API endpoints
- ⚠️ **Missing**: Request/response JSON examples
- ⚠️ **Missing**: Last updated timestamp

## Project Structure

```
affinity-api-docs/
├── AGENTS.md (this file)
├── README.md (project README)
├── .gitignore (gitignore rules)
├── docs/
│   ├── v1/
│   │   └── affinity_api_docs.md (v1 documentation - in progress)
│   └── v2/ (v2 documentation - planned for future)
├── scripts/ (temporary extraction/processing scripts - gitignored)
│   ├── extract_code_examples.py
│   ├── parse_and_add_examples.py
│   └── *.py (all scripts are temporary/throwaway)
├── tmp/ (temporary outputs - gitignored)
│   ├── api_docs_raw.html (fetched HTML)
│   ├── code_blocks.json (extracted code blocks)
│   └── extracted_*.json (other extracted data)
└── .dev/ (development notes - gitignored)
    └── notes.md (development notes)
```

**Key Points:**
- `docs/` - All documentation files (committed to git)
- `scripts/` - **All scripts are temporary/throwaway** (gitignored)
  - These are one-off extraction/processing scripts for this iterative project
  - Once documentation is complete, scripts can be deleted
- `tmp/` - All temporary outputs and extracted data (gitignored)
- `.dev/` - Development notes and scratch files (gitignored)

## Key Tasks Remaining

### 1. Add Code Examples

The live API documentation site includes code examples in multiple languages (cURL, Ruby, Python, Node.js) for each endpoint. These need to be extracted and added to the markdown file.

**Location**: Code examples should be added after each endpoint definition (after `## GET /path` or `## POST /path` etc.) and before the next section.

**Format**: Code examples should follow this structure:

1. Add a `#### Example Request` heading
2. Include code blocks for each available language:
   - `bash` for cURL examples
   - `ruby` for Ruby examples  
   - `python` for Python examples
   - `javascript` for Node.js examples
3. Add a `#### Example Response` heading
4. Include a `json` code block with example response data

Example structure:
- `#### Example Request` section with language-specific code blocks
- `#### Example Response` section with JSON example

### 2. Extract Code Examples from Live Site

The HTML from https://api-docs.affinity.co/ has been fetched and saved. Code examples need to be:
- Parsed from the HTML
- Matched to their corresponding endpoints
- Cleaned of HTML entities and formatting
- Added to the appropriate sections in the markdown

### 3. Add Last Updated Timestamp

The live site includes a "Last updated" timestamp that should be added to the documentation header.

## Code Style & Conventions

- **Markdown**: Use standard markdown formatting
- **Code Blocks**: Use fenced code blocks with language identifiers (bash, ruby, python, javascript, json)
- **Headers**: Use `##` for endpoint definitions, `####` for subsections
- **Tables**: Ensure proper spacing around pipes: `| column | column |`
- **Links**: Use markdown link format: `[text](#anchor)` for internal links
- **Notes**: Use `#### Note` for important notes

## File Locations

- **v1 documentation**: `docs/v1/affinity_api_docs.md` (current focus)
- **v2 documentation**: `docs/v2/` (planned for future)
- **Source HTML**: `tmp/api_docs_raw.html` (temporary, gitignored)
- **Code blocks**: `tmp/code_blocks.json` (temporary, gitignored)
- **Scripts**: `scripts/` directory
- **Temporary outputs**: `tmp/` directory (all gitignored)

## Important Notes

- The markdown files should contain **ALL** information from the web pages, even if in a non-interactive format
- Code examples are critical - they're the most important missing piece for v1
- The documentation should be complete enough for developers to use the API without visiting the live site
- Maintain consistency with existing formatting and structure
- **v1** endpoint paths use the base URL: `https://api.affinity.co/`
- **v2** endpoint paths use the base URL: `https://api.affinity.co/v2`

## Authentication

**Affinity API v1** (this documentation) uses:
- **HTTP Basic Auth**: Provide API key as basic auth password (no username needed)
- **HTTP Bearer Auth**: Also supported - provide API key as bearer token

**Affinity API v2** (separate API, not yet documented here) uses:
- **HTTP Bearer Auth only**: Provide API key as bearer token

All examples in this v1 documentation should use `YOUR_API_KEY` or `$APIKEY` as placeholder.

## Next Steps

1. Parse the fetched HTML to extract code examples
2. Match code examples to their corresponding endpoints
3. Add code examples in all available languages (cURL, Ruby, Python, Node.js)
4. Add example request/response JSON where appropriate
5. Add "Last updated" timestamp to the header
6. Verify all content matches the live documentation site

## Resources

- **v1 API Documentation** (this repo): https://api-docs.affinity.co/
- **v2 API Documentation** (future work): https://developer.affinity.co/
- Support: support@affinity.co

## API Version Differences

- **v1**: Legacy API, uses Basic Auth (no username) or Bearer Auth
- **v2**: New API, uses Bearer Auth only, different terminology and approach
- v2 is **not** a superset of v1 - they are separate APIs with different designs

