#!/usr/bin/env python3
"""Validate minority-erasure JSON records against the public draft schema.

This validator intentionally uses only the Python standard library so GitHub
Actions can run it without dependency installation.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"{path}: invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}") from exc


def location_path(location: str, key: str) -> str:
    if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", key):
        return f"{location}.{key}"
    return f"{location}[{key!r}]"


def validate_schema_document(schema: Any, source: Path) -> list[str]:
    errors: list[str] = []
    if not isinstance(schema, dict):
        return [f"{source}: schema must be a JSON object"]

    required = {"$schema", "$id", "title", "type", "required", "properties"}
    missing = sorted(required - schema.keys())
    if missing:
        errors.append(f"{source}: missing schema fields: {', '.join(missing)}")

    if schema.get("type") != "object":
        errors.append(f"{source}: top-level schema type must be object")

    required_fields = schema.get("required")
    properties = schema.get("properties")
    if not isinstance(required_fields, list) or not all(isinstance(item, str) for item in required_fields):
        errors.append(f"{source}: required must be an array of strings")
    if not isinstance(properties, dict):
        errors.append(f"{source}: properties must be an object")
    elif isinstance(required_fields, list):
        missing_properties = sorted(set(required_fields) - properties.keys())
        if missing_properties:
            errors.append(f"{source}: required fields missing from properties: {', '.join(missing_properties)}")

    return errors


def type_matches(value: Any, expected_type: str) -> bool:
    if expected_type == "object":
        return isinstance(value, dict)
    if expected_type == "array":
        return isinstance(value, list)
    if expected_type == "string":
        return isinstance(value, str)
    if expected_type == "boolean":
        return isinstance(value, bool)
    if expected_type == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected_type == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected_type == "null":
        return value is None
    return False


def validate_value(value: Any, schema: dict[str, Any], location: str, errors: list[str]) -> None:
    expected_type = schema.get("type")
    if isinstance(expected_type, str) and not type_matches(value, expected_type):
        errors.append(f"{location}: expected {expected_type}, got {type(value).__name__}")
        return

    if "const" in schema and value != schema["const"]:
        errors.append(f"{location}: expected constant value {schema['const']!r}")

    enum_values = schema.get("enum")
    if isinstance(enum_values, list) and value not in enum_values:
        errors.append(f"{location}: value {value!r} is not in allowed enum")

    min_length = schema.get("minLength")
    if isinstance(min_length, int) and isinstance(value, str) and len(value) < min_length:
        errors.append(f"{location}: string is shorter than minLength {min_length}")

    min_items = schema.get("minItems")
    if isinstance(min_items, int) and isinstance(value, list) and len(value) < min_items:
        errors.append(f"{location}: array has fewer than minItems {min_items}")

    fmt = schema.get("format")
    if fmt == "date" and isinstance(value, str) and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        errors.append(f"{location}: expected YYYY-MM-DD date")

    if isinstance(value, dict):
        required = schema.get("required", [])
        if isinstance(required, list):
            missing = sorted(item for item in required if isinstance(item, str) and item not in value)
            if missing:
                errors.append(f"{location}: missing required fields: {', '.join(missing)}")

        properties = schema.get("properties", {})
        if isinstance(properties, dict):
            if schema.get("additionalProperties") is False:
                extra = sorted(set(value) - set(properties))
                if extra:
                    errors.append(f"{location}: unexpected fields: {', '.join(extra)}")
            for key, child_value in value.items():
                child_schema = properties.get(key)
                if isinstance(child_schema, dict):
                    validate_value(child_value, child_schema, location_path(location, key), errors)

    if isinstance(value, list):
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, item in enumerate(value):
                validate_value(item, item_schema, f"{location}[{index}]", errors)


def validate_record(record: Any, schema: dict[str, Any], source: Path) -> list[str]:
    errors: list[str] = []
    validate_value(record, schema, str(source), errors)

    if isinstance(record, dict):
        if record.get("synthetic") is True and record.get("real_person_or_case") is not False:
            errors.append(f"{source}: synthetic records must set real_person_or_case to false")
        if record.get("consent", {}).get("publication_approved") is False:
            publication_status = record.get("publication", {}).get("status")
            if publication_status not in {"not_publishable", "restricted"}:
                errors.append(f"{source}: records without publication approval must not be public examples")
        if record.get("human_review", {}).get("completed") is False:
            if record.get("publication", {}).get("evidence_status") == "approved_evidence":
                errors.append(f"{source}: incomplete human review cannot be approved evidence")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--schema", required=True, type=Path)
    parser.add_argument("records", nargs="+", type=Path)
    args = parser.parse_args()

    all_errors: list[str] = []
    try:
        schema = load_json(args.schema)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1

    all_errors.extend(validate_schema_document(schema, args.schema))
    if not isinstance(schema, dict):
        all_errors.append(f"{args.schema}: cannot validate records without an object schema")
    else:
        for record_path in args.records:
            try:
                record = load_json(record_path)
            except ValueError as exc:
                all_errors.append(str(exc))
                continue
            all_errors.extend(validate_record(record, schema, record_path))

    if all_errors:
        for error in all_errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Validated schema: {args.schema}")
    for record_path in args.records:
        print(f"Validated record: {record_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
