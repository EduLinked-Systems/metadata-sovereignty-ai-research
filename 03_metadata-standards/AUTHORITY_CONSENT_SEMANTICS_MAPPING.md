# Authority, Consent and Human-Sovereignty Semantics Mapping

Status: CANDIDATE — HUMAN REVIEW REQUIRED BEFORE NORMATIVE PROMOTION

## Purpose

This document defines the smallest standards-composition boundary needed to prevent EduLinked systems from collapsing consent, permission, authorship, provenance, human authority, interpretation, inference, disclosure and consequential decision use into one field or one machine decision.

It extends no production authority. It does not replace source-owned consent records, legal advice, privacy controls, access control, organisational approval, or person-authored assertions.

## Core invariants

1. CONSENT != PERMISSION != AUTHORITY != PROVENANCE != AUTHORSHIP.
2. Permission to collect information does not imply permission to infer from it.
3. Permission to collect or infer does not imply permission to disclose, publish, train on, or use the information or inference in a consequential decision.
4. A machine inference about a person is not a person-authored assertion.
5. A record holder is not automatically the authority over the subject's perspective, identity, needs or desired outcomes.
6. Human review remains required where legal interpretation, privacy, consent, consequential decisions, public claims or normative ontology promotion are involved.
7. Current consent or authority must not silently rewrite historical consent, authority or provenance.

## Reuse before extension

| Semantic concern | Primary reusable authority | EduLinked treatment |
| --- | --- | --- |
| provenance, generation, attribution, transformation | W3C PROV-O | REUSE; do not create parallel provenance semantics |
| personal-data processing, purpose, consent/legal basis, recipients and processing roles | W3C Data Privacy Vocabulary (DPV) | MAP/REUSE before local extension |
| permissions, prohibitions, duties, actions and constraints | W3C ODRL | MAP/REUSE before local permission vocabulary |
| machine-readable consent record/receipt structure | ISO/IEC TS 27560-aligned model, including DPV guidance where applicable | MAP; do not claim compliance until validated |
| record consent state, authorship role, accessibility flags, redaction and export metadata | existing metadata-sovereignty model | REUSE existing repository controls |
| human Perspective, contextual Need, DesiredOutcome and Contribution | EduLinked Upper Ontology candidate semantics | BIND; do not duplicate here |
| temporal validity | established temporal semantics such as OWL-Time where required | REUSE/MAP |

## Existing repository semantics retained

The existing metadata standards remain authoritative for their current bounded fields, including consent status, author role, accessibility flags, evidence references, change history, redaction and export provenance. This candidate does not rename or expand those controlled vocabularies.

Any normative controlled-vocabulary change must follow the repository's established governance and human approval process.

## Residual human-authority questions

A governed assertion or processing activity should be able to answer, directly or by binding to authoritative records:

- Who or what is the subject?
- Who made the assertion?
- Is the assertion self-authored, externally asserted, evidenced, verified, inferred, disputed or superseded?
- What source or evidence supports it?
- When was it observed, asserted and valid?
- Who has authority to amend or approve the assertion?
- For what purpose may the information be processed?
- Which processing actions are permitted, prohibited or conditional?
- Who may receive it?
- May a machine derive an inference from it?
- If an inference is permitted, may that inference be disclosed?
- May the source information or inference be published?
- May it be used for model training or evaluation?
- May it be used in a consequential decision?
- Is human review mandatory before that use?
- What consent, legal basis, duty or constraint supports each permitted use?

These are separate questions. A positive answer to one must not be propagated automatically to another.

## Human perspective and metadata sovereignty

For human-centred EduLinked records, preserve the distinction between:

- what a person says about themselves;
- what EduLinked records about the person;
- what another organisation or professional asserts;
- what documentary evidence establishes;
- what a machine infers;
- what has been verified by an authorised human or authoritative source.

A projection must preserve the source category and must not render an inference as if it were self-authored fact.

## Participation and lived-experience constraints

The following distinctions must survive downstream application, reporting, learning, CRM and knowledge-graph projections:

- PARTICIPANT != CO_DESIGNER
- ACCESS_RECIPIENT != KNOWLEDGE_HOLDER
- INTERPRETER != TEACHER
- CONTRIBUTOR != BENEFICIARY
- PAID_LIVED_EXPERIENCE_CONTRIBUTION != BENEFICIARY_PARTICIPATION
- HEARING_LED_CONTENT_WITH_AUSLAN != AUSLAN_LED_CONTENT
- SOURCE_LANGUAGE_INSTRUCTION != TRANSLATED_INSTRUCTION

Co-design role, contribution authority and remuneration must not be erased by beneficiary-oriented projections.

## Temporal and revocation behaviour

Consent, permission, authority and relationship state are time-sensitive. Systems consuming these semantics must preserve validity periods and revocation/supersession where the source supports them.

A later state must not destroy the historical state needed to explain what was authorised at the time of a prior action.

## Machine authority boundary

An AI agent may inspect, reconcile, map, flag contradictions, prepare candidate projections and request human review within its authorised execution scope.

It must not, solely from this mapping:

- grant consent;
- infer consent from silence or participation;
- expand a permission to a new purpose;
- treat possession of data as authority to use it;
- convert machine inference into person-authored truth;
- promote an intended future state to current fact;
- authorize disclosure, publication, training or consequential decision use;
- make a protected legal, privacy or consent determination;
- promote candidate vocabulary to normative organisational semantics.

## Example: evolving organisational identity

A person operating a sole-trader business may later establish a company. The model must preserve the distinction between the person, trading/business identity, current legal structure, identifiers issued by authoritative registries, and any intended future organisational state.

An intention to incorporate is not evidence that incorporation has occurred. Historical records must retain the legal/organisational state that was valid when the relevant contract, application, relationship or decision occurred.

## Validation gates before machine-readable implementation

Before adding ontology classes, controlled-vocabulary values, schemas or runtime enforcement:

1. inspect the EduLinked Upper Ontology mapping for overlapping human-perspective semantics;
2. inspect core-machine-objects semantic-family routing and authority/provenance controls;
3. inspect knowledge-graph ownership and projection boundaries;
4. verify the exact DPV and ODRL concepts used for each proposed mapping;
5. validate any ISO/IEC TS 27560 compliance claim separately — this document makes none;
6. test at least one temporal person/organisation proving case and one participant/co-designer proving case;
7. obtain required human approval for normative vocabulary or policy promotion.

## Candidate outcome

If the reuse checks succeed, EduLinked-specific semantics should remain narrow: human Perspective, contextual Need, DesiredOutcome, Contribution, and only those assertion/interpretation/inference/decision-use authority distinctions that cannot be represented safely through composition of existing standards and source-owned controls.

The preferred outcome is composition, not another permission system.