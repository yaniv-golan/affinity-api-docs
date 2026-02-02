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
    json_path.write_text(json.dumps(artifacts.spec, indent=2, sort_keys=True) + "\n", encoding="utf-8")
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
