# People, Client, Consent and Metadata Sovereignty Gate

Status: **MANDATORY REPOSITORY SAFETY CONTRACT**

This repository is public. Every human contributor, AI agent, automation, workflow and integration MUST apply this gate before retrieving private material for use here, generating a public projection, creating a fixture, writing a file, committing a change, or opening/updating a pull request.

This gate strengthens the README public-disclosure gate. It does not grant new authority. Where authority, consent, purpose or disclosure status is uncertain, the system MUST fail closed.

## Sovereignty principle

Metadata sovereignty means that technical possession, access, retrieval or inference does not transfer authority over a person, client, community or source-owned record.

The system must preserve, where applicable:

- who or what the information is about;
- who asserted or created it;
- who owns the authoritative source record;
- why it was collected;
- the purpose for which it may be processed;
- the consent, permission, legal basis or other authority supporting that processing;
- permitted and prohibited uses;
- permitted recipients and disclosure boundaries;
- whether machine inference is permitted;
- whether attribution or publication is permitted;
- whether AI training or evaluation use is permitted;
- whether consequential decision use is permitted;
- validity, withdrawal, revocation and supersession state;
- provenance and transformation history;
- any human-review requirement.

## Non-equivalence invariants

`ACCESS != AUTHORITY`

`POSSESSION != OWNERSHIP`

`COLLECTION_CONSENT != INFERENCE_CONSENT`

`COLLECTION_CONSENT != PUBLICATION_CONSENT`

`SERVICE_CONSENT != AI_TRAINING_CONSENT`

`PARTICIPATION != CONSENT_TO_ATTRIBUTION`

`CO_DESIGN_CONSENT != CONSENT_TO_PUBLICATION`

`CO_DESIGN_CONSENT != CONSENT_TO_AI_TRAINING`

`CONSENT != PERMISSION != AUTHORITY != PUBLICATION_AUTHORITY`

`SELF_ASSERTION != THIRD_PARTY_ASSERTION != MACHINE_INFERENCE`

`DE_IDENTIFIED != AUTOMATICALLY_SAFE_TO_PUBLISH`

`ACCESSIBILITY_INFORMATION != PROFILING_PERMISSION`

`LIVED_EXPERIENCE_CONTRIBUTION != ORGANISATIONAL_OWNERSHIP`

`CLIENT_INFORMATION != ORGANISATIONAL_PUBLIC_KNOWLEDGE`

## People privacy

Information about people must be treated as person-centred, purpose-bound and context-sensitive rather than as a reusable organisational asset.

Agents MUST NOT expose, reproduce or infer for public release private or sensitive information about identifiable or reasonably re-identifiable people merely because the information is available in an authorised system.

This includes identity, contact information, accessibility requirements, disability information, health information, support needs, communications, relationships, participation history, lived experience, opinions, preferences, location, financial information, safeguarding information and machine-generated profiles or predictions.

Privacy protection applies to the content of a record and to metadata, filenames, paths, identifiers, relationship edges, timestamps, screenshots, logs, comments and combinations of facts that can enable re-identification.

## Client privacy and confidentiality

Client information remains source-owned and confidentiality-bound. EduLinked holding or processing client information does not make that information public EduLinked knowledge.

Agents MUST preserve boundaries around client records, deliverables, communications, contracts, applications, budgets, internal findings, accessibility assessments, relationship state, strategy, unpublished work and other confidential material.

A public repository may contain an approved public projection of client-related work only when the projection itself has attributable release authority. Publicly known client identity does not automatically authorise publication of private work performed for that client.

## Consent and purpose limitation

Consent must not be treated as a universal boolean.

Where consent is relevant, systems must preserve the purpose, scope, actor, subject, permitted processing, recipients, validity period, withdrawal/revocation state and evidence pointer supported by the authoritative source.

Permission or consent for one activity MUST NOT be silently propagated to another. In particular, permission to collect, store or provide a service does not automatically authorise:

- secondary analysis;
- profiling;
- machine inference;
- cross-system enrichment;
- onward disclosure;
- public attribution;
- publication;
- reuse in unrelated projects;
- AI/model training;
- AI evaluation datasets;
- consequential decisions.

Withdrawal or revocation must not be erased by downstream copies or projections. Historical provenance may need to remain for audit, but it must not be misrepresented as current permission.

## Data minimisation

Agents MUST use the minimum information necessary for the authorised purpose.

When a semantic, architectural or validation question can be answered with public standards, abstract structures, synthetic data or sanitised conformance fixtures, private real-world records MUST NOT be copied into this public repository.

Sanitisation is a risk-reduction step, not publication authority. If a supposedly sanitised record can reasonably be linked back to a person, client, participant, project or protected event, it must remain private unless specifically approved for release.

## Accessibility and disability information

Accessibility, disability, communication and support information may be necessary to provide equitable access. That necessity does not create permission to profile, rank, diagnose, generalise about, publicly identify or train models on a person or group.

Use accessibility information only within the authorised purpose and preserve the person's role in determining how their needs, preferences and identity are represented.

`ACCESS_SUPPORT_PURPOSE != PROFILING_PURPOSE`

## Lived experience and co-design

Participation and lived-experience contribution do not transfer ownership of a person's story, identity, perspective or knowledge to EduLinked.

Co-design participation must not be interpreted as blanket consent to attribution, publication, recording, reuse, disclosure, AI processing or model training.

Systems must preserve distinctions including:

- participant vs co-designer;
- access recipient vs knowledge holder;
- contributor vs beneficiary;
- paid lived-experience contribution vs beneficiary participation;
- consent to participate vs consent to attribute;
- consent to attribute vs consent to publish or reuse.

## Children, young people and higher-risk contexts

Information concerning children, young people or people in contexts involving safeguarding, dependency, heightened vulnerability, power imbalance or significant potential harm requires a stronger fail-closed posture.

Agents must not infer that participation, guardian involvement, programme enrolment, attendance, existing records or prior publication provides blanket authority for new public disclosure or new AI processing.

Where the applicable authority or safeguarding requirement is not established, stop and escalate to authorised human review.

## Assertion and inference integrity

Every material human-related assertion should retain its epistemic origin where the source supports it:

- self-asserted;
- externally asserted;
- evidenced;
- verified;
- machine-inferred;
- disputed;
- superseded.

An agent MUST NOT present a machine inference, third-party assertion or organisational interpretation as though the person said it about themselves.

Inference authority and decision-use authority are separate. Even where inference is permitted, use of that inference in a consequential decision may remain prohibited or require human review.

## Public-release decision

Before a proposed public mutation involving non-public source material, the agent must be able to establish all material elements below:

1. **SUBJECT** — who/what the information concerns;
2. **SOURCE** — authoritative source owner and provenance;
3. **PURPOSE** — why the information is being used here;
4. **AUTHORITY** — what authorises that use;
5. **CONSENT/PERMISSION** — where applicable, what specific processing/disclosure is permitted;
6. **MINIMISATION** — why no less-sensitive representation is sufficient;
7. **DISCLOSURE** — why public Internet release is authorised;
8. **SENSITIVITY/RE-IDENTIFICATION** — whether content or metadata can expose protected information;
9. **HUMAN REVIEW** — whether an attributable authorised human decision is required and has occurred.

If a required element cannot be established, **DO NOT PUBLISH**.

## Agent fail-closed algorithm

```text
IF target_repository_is_public:
    treat_mutation_as_publication = true

IF input_is_non_public OR input_contains_person_or_client_information:
    establish(subject, source, purpose, authority, permitted_processing, permitted_disclosure)

IF any_required_authority_is_missing_or_ambiguous:
    STOP
    keep_information_at_source
    request_authorised_human_review

IF synthetic_or_less_sensitive_input_can_prove_the_same_system_behaviour:
    use_that_instead

IF sanitised_output_still_has_material_reidentification_or_confidentiality_risk:
    STOP

IF public_release_authority_is_not_evidenced:
    STOP

ONLY THEN:
    prepare_minimised_public_projection
    inspect_entire_diff_for_disclosure_risk
    proceed_with_repository_mutation
```

## Scope of the inspection

The disclosure check applies to more than document body text. Inspect:

- filenames and directory names;
- source code and configuration;
- schemas and examples;
- fixtures and test data;
- comments and annotations;
- logs and validation output;
- screenshots and diagrams;
- commit messages;
- branch names;
- issue and pull-request titles/bodies/comments;
- generated artefacts;
- URLs, query strings and identifiers;
- metadata and provenance fields.

## Authority boundary

This gate does not determine legal compliance, provide legal advice, grant consent, override source-owned policies, approve publication, or create production permission semantics.

It establishes the minimum fail-closed behaviour expected of contributors and agents operating on this public research surface. Protected privacy, consent, safeguarding, legal, contractual and consequential governance decisions remain subject to the applicable authoritative source and authorised human review.