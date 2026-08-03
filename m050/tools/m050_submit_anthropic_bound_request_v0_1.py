#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.error
import urllib.request


ENDPOINT = "https://api.anthropic.com/v1/messages"
ANTHROPIC_VERSION = "2023-06-01"


def write_new(path: Path, data: bytes) -> None:
    if path.exists():
        raise SystemExit(f"refusing to overwrite: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True)
    parser.add_argument("--expected-request-sha256", required=True)
    parser.add_argument("--api-key-file", required=True)
    parser.add_argument("--response", required=True)
    parser.add_argument("--transport-receipt", required=True)
    args = parser.parse_args()

    request_path = Path(args.request)
    response_path = Path(args.response)
    receipt_path = Path(args.transport_receipt)
    if response_path.exists() or receipt_path.exists():
        raise SystemExit("refusing to overwrite provider execution artifacts")

    request_bytes = request_path.read_bytes()
    request_sha256 = hashlib.sha256(request_bytes).hexdigest()
    if request_sha256 != args.expected_request_sha256:
        raise SystemExit("bound request SHA-256 mismatch")
    api_key = Path(args.api_key_file).read_text(encoding="utf-8").strip()
    if not api_key or "\n" in api_key:
        raise SystemExit("API key file must contain one non-empty raw key")

    submitted_at = datetime.now(timezone.utc).isoformat()
    request = urllib.request.Request(
        ENDPOINT,
        data=request_bytes,
        method="POST",
        headers={
            "anthropic-version": ANTHROPIC_VERSION,
            "content-type": "application/json",
            "x-api-key": api_key,
        },
    )
    response_bytes = b""
    status = None
    response_headers = {}
    transport_error = None
    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            status = response.status
            response_bytes = response.read()
            response_headers = dict(response.headers.items())
    except urllib.error.HTTPError as exc:
        status = exc.code
        response_bytes = exc.read()
        response_headers = dict(exc.headers.items())
        transport_error = f"HTTPError:{exc.code}"
    except Exception as exc:
        transport_error = f"{type(exc).__name__}:{exc}"

    if response_bytes:
        write_new(response_path, response_bytes)
    receipt = {
        "schema_version": "M050-ANTHROPIC-TRANSPORT-RECEIPT-0.1",
        "endpoint": ENDPOINT,
        "anthropic_version": ANTHROPIC_VERSION,
        "submitted_at_utc": submitted_at,
        "submission_attempted": True,
        "authorization_consumed": True,
        "request_path": str(request_path),
        "request_sha256": request_sha256,
        "http_status": status,
        "response_path": str(response_path) if response_bytes else None,
        "response_sha256": hashlib.sha256(response_bytes).hexdigest() if response_bytes else None,
        "response_bytes": len(response_bytes),
        "request_id": response_headers.get("request-id"),
        "transport_error": transport_error,
        "api_key_persisted": False,
    }
    write_new(
        receipt_path,
        (json.dumps(receipt, indent=2, sort_keys=True) + "\n").encode("utf-8"),
    )
    print(json.dumps({
        "http_status": status,
        "response_bytes": len(response_bytes),
        "response_sha256": receipt["response_sha256"],
        "transport_error": transport_error,
    }, sort_keys=True))
    return 0 if status is not None and 200 <= status < 300 else 1


if __name__ == "__main__":
    raise SystemExit(main())
