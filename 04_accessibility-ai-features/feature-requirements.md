# Accessibility AI Feature Requirements

Accessibility-focused AI features in this research repository are candidate transformations or assistive capabilities. They are not accessibility authorities and must not create a second Easy Read, AAC, document-accessibility or learner-access architecture.

Possible AI features include:

- plain-language summarisation
- Easy Read materialisation support
- caption and transcript generation
- alternative-text drafting
- translation or localisation assistance where an attributable language-access need exists
- AAC-compatible or symbol-supported representation support where an attributable communication-access need exists

## Reuse the existing EduLinked accessibility authority chain

Before proposing or evaluating an accessibility AI feature, inspect and reuse these existing authorities:

- `EduLinked-Pty-Ltd/core-machine-objects/objects/education/easy-read-adaptive-instructional-composition-v0.1.json` for Easy Read semantic and composition authority.
- `EduLinked-Pty-Ltd/core-machine-objects/objects/accessibility-capability-layer/contracts/accessible-document-lifecycle-v1.json` for source-preserving requirement, transformation, verification, export and participation boundaries.
- `EduLinked-Systems/edulinked-accessibility-system/adapters/easy-read/entrypoints.yaml` for the current Easy Read implementation/navigation projection.
- `EduLinked-Pty-Ltd/accessible-RTO/templates/inclusive-learning-production-standard.md` (`AccessFlow v1.2.0`) for inclusive learning-production requirements, including multilingual, signed-language, Easy Read, AAC, caption, transcript, nonvisual and runtime-accessibility production states.

`EduLinked-Systems/easy-read` remains a successor boundary with an open authority-proof gate. Do not bind production consumers to it until its source-owned proving case resolves that gate.

## Every evaluated feature must record

- intended purpose and source-owned use context
- attributable access requirement or explicit state that no requirement has yet been established
- source artefact and source revision
- required data inputs and sensitivity
- authorship, consent and permitted-use constraints
- transformation type and AI/model provenance where AI is used
- transparency requirements
- selected accessibility or communication modality, if any, and why it is applicable
- production state where relevant
- automated-check state separately from human or assistive-technology verification
- known semantic-loss, translation, summarisation or representation risks
- human/specialist review required before any stronger claim
- participant or cohort validation state where comprehension or real use is material
- publication authority state

## Claim ceilings

Preserve these distinctions:

- `AI_GENERATED != ACCESSIBLE`
- `PLAIN_LANGUAGE != EASY_READ`
- `EMOJI_OR_IMAGE != AAC`
- `TRANSLATED_TEXT != CULTURALLY_LOCALISED`
- `TRANSLATION_VERIFIED != ACCESSIBILITY_VERIFIED`
- `AUTOMATED_CHECK != ACCESSIBILITY_CONFORMANCE`
- `MATERIALISATION != PARTICIPANT_COMPREHENSION`
- `ACCESSIBILITY_OPTION_AVAILABLE != PARTICIPANT_PREFERENCE`
- `ACCESSIBILITY_VERIFICATION != PARTICIPATION_OUTCOME`
- `RESEARCH_RECOMMENDATION != PRODUCTION_OR_PUBLICATION_AUTHORITY`

The research task is to evaluate a feature against the existing authority chain and evidence, not to invent a new accessibility model around the feature.
