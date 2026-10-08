# Public Research Sanitisation Guide

This guide defines the minimum repository process for preparing research material for this public repository. It applies to examples, datasets, case studies, quotations, screenshots, media, exports, and generated derivatives.

It does not establish that material is safe merely because identifiers were removed. Human approval is required before release.

## Default Rule

Prefer wholly synthetic examples. Do not copy, transform, summarise, translate, or otherwise derive a public example from real sensitive or restricted material when a synthetic example can demonstrate the same research point.

The following statements are not equivalent:

`SYNTHETIC_EXAMPLE != DE-IDENTIFIED_REAL_RECORD`

`IDENTIFIERS_REMOVED != REIDENTIFICATION_RISK_RESOLVED`

`SANITISED != PUBLICATION_APPROVED`

`VALIDATION_PASSED != HUMAN_APPROVAL`

## Material That Must Not Be Published

Do not publish:

- real case records, evidence registers, interviews, incident details, or chain-of-custody material
- direct identifiers or combinations of details that could identify a person or small community
- audio, video, images, screenshots, document properties, comments, revision history, or hidden content relating to real people
- legal, forensic, clinical, medical, safeguarding, or other restricted notes
- internal repository, Drive, SharePoint, system, credential, or access details
- material without evidenced permission, lawful authority, or compatible reuse rights

When classification or authority is uncertain, stop and treat the material as non-public.

## Release Workflow

1. **Classify the material.** Apply [DATA_CLASSIFICATION.md](DATA_CLASSIFICATION.md). Record whether the proposed artefact is synthetic, derived from public sources, or derived from non-public material.
2. **Minimise the source.** Use only the information needed for the research purpose. Prefer a new synthetic example over redaction of a real record.
3. **Check identity risk.** Review names, contact details, dates, locations, organisations, rare events, quotations, filenames, URLs, identifiers, and combinations that could permit reidentification.
4. **Check embedded and derived content.** Inspect document properties, comments, tracked changes, hidden sheets/slides, image metadata, linked files, filenames, generated summaries, translations, and accessible-format derivatives.
5. **Check authority and rights.** Confirm consent or other publication authority, attribution, licence, copyright, cultural and community authority, and any limits on AI processing or transformation.
6. **Preserve meaning and accessibility.** Confirm that redaction or transformation does not misrepresent authorship, consent, evidence, community meaning, or accessibility needs. Generated accessible formats require human review.
7. **Complete the publication gate.** Use [PUBLICATION_CHECKLIST.md](PUBLICATION_CHECKLIST.md) for the exact artefact and version proposed for release.
8. **Obtain human approval.** The approving person must have authority for the material and destination. Repository validation and pull-request review do not independently grant publication authority.
9. **Record the decision.** Add a privacy-safe entry to [PUBLICATION_LOG.md](PUBLICATION_LOG.md). Never place confidential source locations, personal data, or redaction details in the public log.
10. **Recheck changes.** A material revision, new format, new destination, changed consent state, or changed licence requires a new review.

## Labelling Public Examples

Use one accurate label:

- **Synthetic example - created for testing; no real person or case.**
- **Public-source example - derived only from the cited public sources; reviewed for reuse rights.**
- **Sanitised example - derived from non-public material; human-reviewed for this exact public release.**

Do not label a real-derived artefact as synthetic. Do not use "sanitised" as a substitute for an approval record.

## Withdrawal and Correction

If consent, authority, accuracy, sensitivity, or reidentification risk changes:

1. stop further reuse and publication
2. notify the repository maintainer through an appropriate non-public channel
3. remove or restrict the affected projection where authorised
4. preserve a minimal, privacy-safe correction or withdrawal record
5. reassess downstream copies and derivatives

Do not add sensitive details to a public issue while requesting removal.

## Evidence Boundary

The checklist and log record that a human gate was completed. They do not prove legal compliance, eliminate reidentification risk, transfer source authority, approve a private product release, or authorise publication to another destination.
