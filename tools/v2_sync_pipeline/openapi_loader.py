"""Download and parse the Affinity API v2 OpenAPI specification."""
from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any
from urllib.parse import urljoin
import hashlib

import requests
from bs4 import BeautifulSoup

DEFAULT_URL = "https://developer.affinity.co/"
STATE_SCRIPT_PREFIX = "/docs/v2/redocly-state"


@dataclass
class FetchArtifacts:
    html: str
    state_js: str
    fetched_at: datetime
    last_modified: datetime | None
    state_url: str
    date_header: datetime | None


@dataclass
class SavedArtifacts:
    html_path: Path
    state_path: Path
    json_path: Path
    hash_manifest: Path


def fetch_site(url: str = DEFAULT_URL) -> FetchArtifacts:
    """Fetch the Redoc shell HTML and state JS."""
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    fetched_at = datetime.now(timezone.utc)
    last_modified_dt = _parse_http_date(response.headers.get("Last-Modified"))
    date_header = _parse_http_date(response.headers.get("Date"))
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    script_tag = soup.find("script", src=lambda value: value and value.startswith(STATE_SCRIPT_PREFIX))
    if not script_tag or not script_tag.get("src"):
        raise RuntimeError("Unable to locate the Redoc state script on the v2 docs page.")
    state_url = urljoin(url, script_tag["src"])
    state_resp = requests.get(state_url, timeout=30)
    state_resp.raise_for_status()
    return FetchArtifacts(
        html=html,
        state_js=state_resp.text,
        fetched_at=fetched_at,
        last_modified=last_modified_dt,
        date_header=date_header,
        state_url=state_url,
    )


def extract_openapi_from_state(state_js: str) -> dict[str, Any]:
    """Extract OpenAPI JSON from the Redoc state JS file."""
    marker = "JSON.parse("
    try:
        start = state_js.index(marker) + len(marker)
        end = state_js.rindex(")")
    except ValueError as exc:
        raise RuntimeError("Unable to locate JSON payload inside redoc state script.") from exc
    json_blob = state_js[start:end]
    if json_blob.startswith('"') and json_blob.endswith('"'):
        json_blob = json_blob[1:-1]
    payload = json_blob.encode("utf-8").decode("unicode_escape")
    data = json.loads(payload)
    return data["definition"]["data"]


def save_artifacts(artifacts: FetchArtifacts, spec: dict[str, Any], snapshot_dir: Path) -> SavedArtifacts:
    """Persist raw HTML, state JS, and parsed JSON for auditing."""
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    html_path = snapshot_dir / "developer_affinity_co.html"
    state_path = snapshot_dir / "redoc_state.js"
    json_path = snapshot_dir / "openapi.json"
    html_path.write_text(artifacts.html, encoding="utf-8")
    state_path.write_text(artifacts.state_js, encoding="utf-8")
    json_path.write_text(json.dumps(spec, indent=2, sort_keys=True), encoding="utf-8")
    manifest_path = snapshot_dir / "artifact_hashes.json"
    hashes = {
        "html_sha256": _hash_file(html_path),
        "state_sha256": _hash_file(state_path),
        "openapi_sha256": _hash_file(json_path),
        "state_url": artifacts.state_url,
        "fetched_at_iso": artifacts.fetched_at.isoformat(),
        "last_modified_iso": artifacts.last_modified.isoformat() if artifacts.last_modified else None,
        "date_header_iso": artifacts.date_header.isoformat() if artifacts.date_header else None,
    }
    manifest_path.write_text(json.dumps(hashes, indent=2, sort_keys=True), encoding="utf-8")
    return SavedArtifacts(
        html_path=html_path,
        state_path=state_path,
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
