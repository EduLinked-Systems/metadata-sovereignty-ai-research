# CONTROLLED_VOCABULARIES.md

This file defines the canonical controlled vocabularies used by the Metadata Sovereignty Alliance (msa) metadata schema. Publish this file alongside `STANDARDS_MAPPING.md`. Use these vocabularies for validation, UI dropdowns, and JSON-LD URIs when programmatic validation is required.

**Namespace suggestion (example):** `https://example.org/msa/vocab#`  
*(Replace with your production namespace if available.)*

---

## How to use these vocabularies

- **Human-readable prototypes:** you may use plain strings (for example, `"granted"`).  
- **Programmatic / JSON-LD usage:** prefer full term URIs, for example:
  ```json
  "msa:consentStatus": "https://example.org/msa/vocab#granted"

and include the vocabulary namespace in @context when compacting.

When adding a new vocabulary term

Add a label, short definition and example usage to this file.

Add the term URI under your msa vocab namespace (or an approved public vocabulary).

Update STANDARDS_MAPPING.md if the new term affects mappings.

Add a changelog entry (see maintenance section).

File metadata

File: /03_metadata-standards/CONTROLLED_VOCABULARIES.md

Version: v1.0

Last updated: 2026-03-12
(Update these values whenever you change the vocabularies.)

1. consent_status (msa:consentStatus)

Purpose: Describes the current state of consent for use of the record and permitted processing.

Terms & short definitions

msa:granted — Consent granted for the stated uses.

msa:limited — Consent granted for limited / restricted uses (document scope).

msa:withdrawn — Previously granted consent now withdrawn; data requires restriction or removal.

msa:unknown — Consent not recorded or unknown.

Examples

JSON-LD (string form):

"msa:consentStatus": "msa:granted"

Human-readable:

consent_status: "granted"
2. author_role (msa:authorRole)

Purpose: Identifies the role of the person or agent associated with authorship or contribution.

Terms & short definitions

msa:self-advocate — First-person author (the person whose experience the record documents).

msa:advocate — Advocate acting on behalf of someone else.

msa:researcher — Research team member or analyst.

msa:supervisor — Supervisor or governance reviewer.

msa:clinician — Clinical professional (if present).

msa:community-member — Community contributor or witness.

Example (JSON-LD):

"msa:authorRole": "msa:self-advocate"
3. accessibility_flags (msa:accessibilityFlag)

Purpose: Declares which accessible formats or accessibility conversions exist (or are required) for a record or export.

Terms & short definitions

msa:EasyRead — Easy-Read format available (plain language + visuals).

msa:Captioned — Captions available for media.

msa:Auslan — Auslan / signed interpretation available.

msa:AAC — AAC-compatible version or symbol set available.

msa:PlainLanguage — Plain-language summary available.

msa:Transcript — Full transcript available for audio/video.

Usage notes

A record may list multiple flags.

For public outputs, at least one accessibility flag should be present.

Example

"msa:accessibilityFlags": ["msa:EasyRead", "msa:Captioned"]
4. evidence_redaction_reason (msa:redactionReason)

Purpose: Categorical reason codes describing why evidence or parts of records were redacted.

Terms & short definitions

msa:pii — Redacted due to personal identifying information.

msa:legal — Redacted for legal or forensic reasons.

msa:safety — Redacted to protect safety of an individual or community.

msa:consent — Redacted because consent for public release is not present.

Example

"msa:evidenceRedactions": [{"id":"EVID-0001","reason":"msa:pii"}]
5. watermark_indicator (msa:watermarkIndicator)

Purpose: Indicates whether the record or artifact carries an authorship watermark, fingerprint or embedded provenance token.

Terms & short definitions

msa:watermarkPresent — A visible or embedded watermark/fingerprint is present.

msa:watermarkNone — No watermark present.

Example

"msa:watermarkIndicator": "msa:watermarkPresent"
6. export_sanitisation_status (msa:sanitisationStatus)

Purpose: Tracks whether an exported artifact was sanitised for public release.

Terms & short definitions

msa:sanitised_full — Fully sanitised and safe for public release.

msa:sanitised_partial — Partially sanitised; internal review or supervisor approval required before public release.

msa:not_sanitised — Not sanitised (internal use only).

Example

"msa:exportProvenance": {"agent":"Exporter v1.0","date":"2026-03-12","sanitisation":"msa:sanitised_full"}
7. Suggested term URIs (examples)

Use these examples when encoding vocabularies as URIs. Replace the domain with your canonical domain if available.

https://example.org/msa/vocab#granted

https://example.org/msa/vocab#limited

https://example.org/msa/vocab#withdrawn

https://example.org/msa/vocab#self-advocate

https://example.org/msa/vocab#EasyRead

8. Validation & governance notes

Versioning: When a vocabulary changes, increment version in this file and add a changelog entry.

Machine validation: For production, expose a JSON or TTL vocabulary file that systems can load. For student projects, the Markdown file suffice.

Extensibility: Propose new terms via Issues. New terms must include label, definition, example, and supervisor approval before public use.

Changelog template: Each change entry should include {date, author, termAdded/termUpdated, briefReason} and be appended at the end of this document.

9. Compact JSON-LD example using URIs
{
  "@context": {
    "msa_vocab": "https://example.org/msa/vocab#"
  },
  "msa:consentStatus": "https://example.org/msa/vocab#granted",
  "msa:authorRole": "https://example.org/msa/vocab#self-advocate",
  "msa:accessibilityFlags": [
    "https://example.org/msa/vocab#EasyRead",
    "https://example.org/msa/vocab#Captioned"
  ]
}
10. Maintenance

Keep the vocabulary list minimal and well-documented.

Add a one-line changelog entry each time terms are added/modified.

Ensure that any term used in public examples appears here with a definition and example usage.
