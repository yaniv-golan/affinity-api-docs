"""Download and parse the Affinity API v2 OpenAPI specification."""
from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any
import hashlib

import requests

# Affinity migrated from Redoc to Mintlify in early 2026.
# The OpenAPI spec is now served directly as JSON.
DEFAULT_URL = "https://developer.affinity.co/api-reference/openapi.json"

# The current API version is served only as openapi.json. Older (locked) versions are served at
# openapi-<version>.json and mirrored for change tracking. When Affinity ships a new version, add the
# previous current version here and bump CURRENT_API_VERSION (the sync warns when they drift).
CURRENT_API_VERSION = "2026-09-17"
VERSIONED_SPECS: tuple[str, ...] = ("2026-07-15", "2024-01-01")
VERSIONED_SPEC_URL = "https://developer.affinity.co/api-reference/openapi-{version}.json"


class SpecFetchError(RuntimeError):
    """Raised when a versioned spec cannot be fetched or is not the expected version."""


def fetch_versioned_spec(version: str, timeout: int = 60) -> dict[str, Any]:
    """Fetch a locked API version's OpenAPI spec and check it is what we asked for."""
    url = VERSIONED_SPEC_URL.format(version=version)
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        spec = response.json()
    except (requests.RequestException, ValueError) as exc:
        raise SpecFetchError(f"{url}: {exc}") from exc
    found = (spec.get("info") or {}).get("x-affinity-api-version") if isinstance(spec, dict) else None
    if found != version:
        raise SpecFetchError(f"{url}: expected x-affinity-api-version {version!r}, got {found!r}")
    if not spec.get("paths"):
        raise SpecFetchError(f"{url}: spec has no paths")
    return spec


def serialize_spec(spec: dict[str, Any]) -> bytes:
    """Stable serialization shared by every committed spec (sorted keys, 2-space indent)."""
    return (json.dumps(spec, indent=2, sort_keys=True) + "\n").encode("utf-8")


@dataclass
class FetchArtifacts:
    spec: dict[str, Any]
    fetched_at: datetime
    last_modified: datetime | None
    date_header: datetime | None
    source_url: str


@dataclass
class SavedArtifacts:
    json_path: Path
    hash_manifest: Path


def fetch_site(url: str = DEFAULT_URL) -> FetchArtifacts:
    """Fetch the OpenAPI spec directly from Mintlify."""
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    fetched_at = datetime.now(timezone.utc)
    last_modified_dt = _parse_http_date(response.headers.get("Last-Modified"))
    date_header = _parse_http_date(response.headers.get("Date"))
    spec = response.json()
    return FetchArtifacts(
        spec=spec,
        fetched_at=fetched_at,
        last_modified=last_modified_dt,
        date_header=date_header,
        source_url=url,
    )


def save_artifacts(artifacts: FetchArtifacts, snapshot_dir: Path) -> SavedArtifacts:
    """Persist OpenAPI JSON for auditing."""
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    json_path = snapshot_dir / "openapi.json"
    json_path.write_bytes(serialize_spec(artifacts.spec))
    manifest_path = snapshot_dir / "artifact_hashes.json"
    hashes = {
        "openapi_sha256": _hash_file(json_path),
        "source_url": artifacts.source_url,
        "fetched_at_iso": artifacts.fetched_at.isoformat(),
        "last_modified_iso": artifacts.last_modified.isoformat() if artifacts.last_modified else None,
        "date_header_iso": artifacts.date_header.isoformat() if artifacts.date_header else None,
    }
    manifest_path.write_text(json.dumps(hashes, indent=2, sort_keys=True), encoding="utf-8")
    return SavedArtifacts(
        json_path=json_path,
        hash_manifest=manifest_path,
    )


def _hash_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _parse_http_date(value: str | None) -> datetime | None:
    if not value:
        return None
    dt = parsedate_to_datetime(value)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)
