# Organisation Workflow — Public Summary

This document explains the organisation workflow at a high level so student teams understand realistic assumptions when designing metadata, AI features and governance.

> Note: Operational details that could identify individuals, case IDs or internal storage locations are **deliberately omitted**. Those items remain private.

## How records are created (public assumptions)

- Records are typically authored in cloud documents (Google Docs / SharePoint) and edited collaboratively. Final approved copies are exported as PDFs for archival.
- At point of creation, authors are expected to capture essential metadata (see `METADATA_TEMPLATE.md`): author role, creation date, purpose, consent status, version number and accessibility flags.
- Versioning convention: `v1`, `v2`, etc. Significant updates should increment major/minor version and note initials + date in the change history.

## Provenance and exports

- An internal registry maps canonical document locations and product IDs (this registry is private). Students should design export formats that **embed** authorship and consent statements rather than rely on external registries.
- Exports intended for public use must preserve authorship attribution and include a short provenance note (author, creation date, version, export date, and whether the export was sanitised).

## Accessibility and outputs

- Accessibility is treated as default: exports should include Easy-Read, plain-language summaries, captions or Auslan scripts where appropriate.
- AI-generated accessibility artefacts must include a human-review step before publication.

## Evidence and sensitive data

- Any record referencing evidence, chain-of-custody, or legal/forensic notes is sensitve and must **not** be in the public repo. Public examples must be fictionalised and sanitised.

## Technology & dataflow (public assumptions)

- Students may assume a metadata-first architecture where metadata is captured at creation, stored alongside records, and used to govern downstream AI processing.
- AI work should be layered on top of well-governed records (i.e., AI does not replace authorship or decision-making).

## Contact & approvals

- For access to private organisational content, students should open a GitHub Issue named `access-request` and explain the rationale; such requests require supervisor approval (founder@edulinked.com.au).
