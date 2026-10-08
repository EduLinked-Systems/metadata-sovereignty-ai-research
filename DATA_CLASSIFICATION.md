# Data Classification and Public Sharing Rules

This document defines data classes and what may be included in this public repository. Classification is a threshold decision, not publication approval. Material classified `PUBLIC` still requires the human gate in [PUBLICATION_CHECKLIST.md](PUBLICATION_CHECKLIST.md).

## Classes

### PUBLIC

- Non-sensitive templates containing field names only
- Project descriptions at a conceptual level
- Accessibility resources and public standards with compatible reuse rights
- Wholly synthetic examples labelled "Synthetic example - created for testing; no real person or case"
- Sanitised examples approved for the exact artefact, version, purpose, format, and destination

### INTERNAL

- Internal governance notes, process details, or staff-only guidance
- Documents that reference internal Drive, SharePoint, repository, system, or access identifiers
- Draft sanitisation and approval evidence that is not suitable for public release

### SENSITIVE / RESTRICTED

- Real case records, evidence registers, interviews, incident details, or chain-of-custody material
- Personal information or combinations of details that could identify a person or small community
- Audio, video, images, or other media of real people without specific publication authority
- Legal, forensic, clinical, medical, or safeguarding notes
- Credentials, secrets, private access details, or protected system information

## Required Rules

1. Never publish `INTERNAL` or `SENSITIVE / RESTRICTED` material in this repository.
2. Prefer wholly synthetic examples. Removing names from a real record does not make it synthetic or automatically safe.
3. Follow [SANITISATION_GUIDE.md](SANITISATION_GUIDE.md) for every example, dataset, case study, quotation, screenshot, media item, export, or generated derivative proposed for public release.
4. Complete [PUBLICATION_CHECKLIST.md](PUBLICATION_CHECKLIST.md) for the exact artefact and version.
5. Record the attributable, privacy-safe human decision in [PUBLICATION_LOG.md](PUBLICATION_LOG.md).
6. Treat uncertain classification, consent, authority, rights, or reidentification risk as a stop condition.
7. Do not place personal data, confidential source locations, or restricted redaction details in public issues, checklists, or logs.

`PUBLIC_CLASSIFICATION != PUBLICATION_APPROVAL`

`IDENTIFIERS_REMOVED != SAFE_TO_PUBLISH`

`PULL_REQUEST_MERGED != HUMAN_RELEASE_AUTHORITY`
