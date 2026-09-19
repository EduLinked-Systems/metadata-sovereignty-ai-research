# AI Boundaries & High-Risk Practices — Public Guidance

This document summarises AI practices that are **prohibited** for this project, and the reasoning behind each prohibition.

> These rules protect participants and contributors, preserve trust, and reduce legal, ethical and accessibility risk. Students must reference these constraints in their ethics checklist.

## Prohibited uses

1. **Biometric profiling (including facial recognition)**
   - Rationale: high risk of misidentification, surveillance harms, and disproportionate impact on vulnerable people.
2. **Automated clinical or legal decision-making**
   - Rationale: black-box decisions can cause harm, remove protected human judgement, and create liability.
3. **Predictive risk scoring about individuals without strong human authority, evidence and an applicable lawful/consented basis**
   - Rationale: such models can encode bias, stigmatise people, and produce consequential exclusion.
4. **Training models on raw sensitive records without explicit, auditable authority for that use**
   - Rationale: training on survivor-authored, participant-authored or sensitive records risks re-identification and can exceed consent or permitted purpose.
5. **Publishing raw case data or protected evidence**
   - Rationale: privacy and safety. Do not expose PII, protected evidence registers, or chain-of-custody details publicly.
6. **Treating AI-generated accessibility output as accessibility conformance or participant comprehension evidence**
   - Rationale: generation, production, automated checking, specialist verification, participant validation and publication are different evidence states.

## Allowed approaches with safeguards

### Accessibility assistance

Accessibility assistance may include summarisation, draft Easy Read materialisation support, caption/transcript generation, alternative-text drafting, translation/localisation assistance, or AAC-compatible representation support.

It is allowed only when:

- the source artefact, source authority and revision are identifiable;
- authorship, consent/permitted-purpose and publication constraints are explicit;
- an accessibility, communication or language requirement is attributable where the feature is being applied for a specific person/cohort/context, or the requirement state is explicitly `UNKNOWN`/`NOT_YET_ESTABLISHED` rather than invented;
- the transformation remains traceable to source meaning and records AI/model provenance where AI is used;
- the existing EduLinked accessibility authority chain is reused rather than replaced;
- automated checks are recorded below the accessibility-conformance ceiling;
- required human, specialist, assistive-technology or participant review remains outstanding until actually evidenced; and
- an authorised human publication decision is required before public release where publication is protected.

Applicable existing EduLinked authorities include:

- `EduLinked-Pty-Ltd/core-machine-objects/objects/education/easy-read-adaptive-instructional-composition-v0.1.json` for Easy Read semantic/composition authority;
- `EduLinked-Pty-Ltd/core-machine-objects/objects/accessibility-capability-layer/contracts/accessible-document-lifecycle-v1.json` for source-preserving requirement, transformation, verification, export and participation boundaries;
- `EduLinked-Systems/edulinked-accessibility-system/adapters/easy-read/entrypoints.yaml` for the current Easy Read implementation/navigation projection; and
- `EduLinked-Pty-Ltd/accessible-RTO/templates/inclusive-learning-production-standard.md` (`AccessFlow v1.2.0`) for inclusive production requirements.

`EduLinked-Systems/easy-read` remains a successor boundary with an open authority-proof gate and is not a production authority merely because the repository exists.

### Retrieval-based systems

Retrieval-based systems (RAG) may be used for research augmentation only when source access is authorised, sources are auditable, provenance is attached, generated synthesis is distinguishable from source text, and any protected publication/decision use remains human-governed.

## Required mitigation steps for any AI feature

- Capture and preserve consent or permitted-use metadata for the proposed processing purpose.
- Mark AI-assisted outputs with source citation, transformation provenance, model/tool where relevant, generation timestamp, and review status.
- Preserve source authority and transformation history; do not silently overwrite the source with a derivative.
- Provide correction, appeal, withdrawal or supersession pathways where the source authority supports them.
- Prefer vendor-agnostic architectures and document fallback/export procedures.
- Keep requirement, implementation, verification, publication and real-use outcomes as separate states.
- Treat language translation/localisation, Easy Read, AAC/symbol support and signed-language work as specialist or participant-informed domains where stronger claims require attributable evidence.

## Claim ceilings

- `AI_GENERATED != ACCESSIBLE`
- `PLAIN_LANGUAGE != EASY_READ`
- `EMOJI_OR_IMAGE != AAC`
- `TRANSLATED_TEXT != CULTURALLY_LOCALISED`
- `AUTOMATED_CHECK != ACCESSIBILITY_CONFORMANCE`
- `HUMAN_REVIEW != PARTICIPANT_COMPREHENSION`
- `ACCESSIBILITY_OPTION_AVAILABLE != PARTICIPANT_PREFERENCE`
- `ACCESSIBILITY_VERIFICATION != PARTICIPATION_OUTCOME`
- `RESEARCH_VALIDATION != PUBLICATION_APPROVAL`

Students must surface these boundaries in the ethics checklist and explain how their proposals enforce them through the existing source-owned architecture.
