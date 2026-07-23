#!/usr/bin/env python3
"""Validate governed metadata-sovereignty research records without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

REQUIRED_TOP_LEVEL = {
    "contract_version",
    "record_id",
    "record_type",
    "title",
    "authorship",
    "provenance",
    "consent",
    "accessibility",
    "ai_permissions",
    "human_review",
    "publication",
    "integrity",
}

RECORD_TYPES = {
    "research_question",
    "source",
    "evidence",
    "finding",
    "recommendation",
    "dataset",
    "publication",
}

AI_PERMISSION_FIELDS = {
    "summarise",
    "translate",
    "accessibility_transform",
    "derive",
    "training",
    "commercial_use",
    "citation_required",
}


def require_fields(value: dict[str, Any], fields: set[str], location: str, errors: list[str]) -> None:
    missing = sorted(fields - value.keys())
    if missing:
        errors.append(f"{location}: missing required fields: {', '.join(missing)}")


def validate_record(record: Any, source: Path) -> list[str]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return [f"{source}: record must be a JSON object"]

    require_fields(record, REQUIRED_TOP_LEVEL, str(source), errors)
    if errors:
        return errors

    if record["contract_version"] != "0.1.0":
        errors.append(f"{source}: contract_version must be 0.1.0")

    record_id = record["record_id"]
    if not isinstance(record_id, str) or not re.fullmatch(r"msr:[a-z0-9][a-z0-9._:-]+", record_id):
        errors.append(f"{source}: record_id must use the msr: identifier pattern")

    if record["record_type"] not in RECORD_TYPES:
        errors.append(f"{source}: unsupported record_type {record['record_type']!r}")

    if not isinstance(record["title"], str) or len(record["title"].strip()) < 3:
        errors.append(f"{source}: title must contain at least three characters")

    authorship = record["authorship"]
    if not isinstance(authorship, dict):
        errors.append(f"{source}: authorship must be an object")
    else:
        require_fields(authorship, {"primary_author", "organisation"}, f"{source}.authorship", errors)

    provenance = record["provenance"]
    if not isinstance(provenance, dict):
        errors.append(f"{source}: provenance must be an object")
    else:
        require_fields(
            provenance,
            {"source_type", "source_references", "derivation_status"},
            f"{source}.provenance",
            errors,
        )
        references = provenance.get("source_references")
        if not isinstance(references, list) or not references:
            errors.append(f"{source}.provenance: source_references must contain at least one reference")

    consent = record["consent"]
    if not isinstance(consent, dict):
        errors.append(f"{source}: consent must be an object")
    else:
        require_fields(consent, {"status", "scope"}, f"{source}.consent", errors)
        if consent.get("status") == "withdrawn" and record["publication"].get("status") in {"approved", "published"}:
            errors.append(f"{source}: withdrawn consent cannot coexist with approved or published status")

    accessibility = record["accessibility"]
    if not isinstance(accessibility, dict):
        errors.append(f"{source}: accessibility must be an object")
    else:
        require_fields(accessibility, {"status", "formats"}, f"{source}.accessibility", errors)

    permissions = record["ai_permissions"]
    if not isinstance(permissions, dict):
        errors.append(f"{source}: ai_permissions must be an object")
    else:
        require_fields(permissions, AI_PERMISSION_FIELDS, f"{source}.ai_permissions", errors)
        for field in AI_PERMISSION_FIELDS:
            if field in permissions and not isinstance(permissions[field], bool):
                errors.append(f"{source}.ai_permissions.{field}: value must be boolean")

    review = record["human_review"]
    if not isinstance(review, dict):
        errors.append(f"{source}: human_review must be an object")
    else:
        require_fields(review, {"required", "status"}, f"{source}.human_review", errors)
        if review.get("required") is True and record["publication"].get("status") in {"approved", "published"}:
            if review.get("status") != "approved":
                errors.append(f"{source}: approved or published records requiring review must have approved human review")

    publication = record["publication"]
    if not isinstance(publication, dict):
        errors.append(f"{source}: publication must be an object")
    else:
        require_fields(publication, {"status", "authority"}, f"{source}.publication", errors)
        if publication.get("authority") == "not_authorised" and publication.get("status") in {"approved", "published"}:
            errors.append(f"{source}: publication is approved or published without publication authority")

    integrity = record["integrity"]
    if not isinstance(integrity, dict):
        errors.append(f"{source}: integrity must be an object")
    else:
        require_fields(integrity, {"version", "content_hash_status"}, f"{source}.integrity", errors)
        if integrity.get("content_hash_status") == "mismatch":
            errors.append(f"{source}: integrity check reports a content hash mismatch")

    return errors


def main(paths: list[str]) -> int:
    targets = [Path(path) for path in paths] if paths else sorted(Path("examples").glob("*.json"))
    if not targets:
        print("No metadata sovereignty records found", file=sys.stderr)
        return 2

    errors: list[str] = []
    for target in targets:
        try:
            record = json.loads(target.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{target}: unable to read valid JSON: {exc}")
            continue
        errors.extend(validate_record(record, target))

    if errors:
        print("Metadata sovereignty validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(targets)} metadata sovereignty record(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
