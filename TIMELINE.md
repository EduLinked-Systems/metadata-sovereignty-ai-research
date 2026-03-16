# Project Timeline — 3-Week Sprint (Compressed)

This timeline is the compressed 3-week schedule students should use when the engagement is limited to three weeks.
It maps clearly to the Project Expectations and the deliverables the team must complete.

> Note: This compressed plan preserves the core deliverables (metadata schema, 2–3 workflows, 3 accessibility AI feature specs, ethics checklist, short roadmap, final report). Allocate time for supervision and human review of AI outputs.

---

## Week 1 — Prepare & Research (Orientation + Foundations)
**Focus:** orientation, background research, early schema thinking.

- Day 1
  - Project kick-off, read repo files: `STUDENT_RESEARCH_GUIDE.md`, `RESEARCH_QUESTIONS.md`, `METADATA_TEMPLATE.md`, `AI_FEATURE_EVALUATION_TEMPLATE.md`
  - Create Project board (Projects / Issues) and assign roles.

- Days 2–3
  - Background research: AI trends & accessibility (deliver: short briefs)
    - AI trends (RAG, explainability, privacy-preserving ML)
    - Accessibility landscape: Easy-Read, AAC, WCAG basics

- Days 4–5
  - Metadata standards review & minimum checklist draft
    - Compare 2–3 standards (Dublin Core, PROV-O, PREMIS)
    - Produce **minimum metadata checklist** (author, role, creation date, consent status, version, change history, accessibility flags)
  - Deliverable (end Week 1): Background briefs + Minimum Metadata Checklist (place in `/02_background_research/` and `/03_metadata-standards/`)

---

## Week 2 — Design & Prototype (Schema, Workflows, AI Features)
**Focus:** authoring the metadata schema, workflows, and accessibility AI specs.

- Days 6–7
  - Finalise metadata schema (map to at least one recognised standard)
  - Create 2 record lifecycle workflows (Create → Update → Review → Export)

- Days 8–9
  - Accessibility AI feature specs (pick 3): for each, produce AI_FEATURE_EVALUATION_TEMPLATE.md entries
    - Example features: Plain-language summariser, Easy-Read generator, Caption generator
  - For each feature: list required metadata, transparency requirements, and mandatory human-review checkpoints.

- Day 10
  - Test schema/workflow using the sanitised example records in `/example_records/`
  - Deliverable (end Week 2): Metadata schema file, workflows, 3 completed AI feature evaluations.

---

## Week 3 — Ethics, Roadmap & Final Report
**Focus:** ethics, metrics, implementation roadmap, finishing final report.

- Days 11–12
  - Ethics checklist & evaluation metrics (pass/fail criteria; measurable indicators such as metadata completeness, readability score, authorship visibility)
  - Map each AI feature to ethics checks and mitigation steps

- Day 13
  - Implementation roadmap (short/medium/long term)
    - Include low-connectivity / offline options and vendor-agnostic recommendations

- Day 14–15
  - Produce final report (8–12 pages + appendices)
    - Executive summary (1 page)
    - Background research (concise)
    - Metadata schema + mapping to standards
    - Accessibility AI feature specs
    - Ethics checklist & evaluation metrics
    - Implementation roadmap
  - Prepare a 10–15 minute presentation or recorded walk-through for supervisors

**Deliverable (end Week 3):** Final report + appendices + short presentation.

---

## Recommended Time Allocation & Team Tips

- Reserve at least **one full day** in Week 3 for supervisor review and revisions.  
- Assign one person to be "metadata owner", one to lead accessibility AI research, one to lead ethics/governance and one to compile the final report. Roles can be combined if fewer students.  
- Use GitHub Issues for each research task and link them to Project cards so supervisors can track progress.

---

## Why 3 weeks is realistic
EduLinked’s tiered planning recognises 2–4 week discovery/prototype phases. The 3-week sprint compresses discovery → prototype → recommendations into a tight but deliverable-focused schedule consistent with internal rapid-prototype phases. Supervisors should prioritise clarity and scope control (avoid chasing extra case studies). :contentReference[oaicite:1]{index=1}
