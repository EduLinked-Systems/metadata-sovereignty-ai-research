# AI Boundaries & High-Risk Practices — Public Guidance

This document summarises AI practices that are **prohibited** for this project, and the reasoning behind each prohibition.

> These rules protect survivors, preserve trust, and reduce legal/ethical risk. Students must reference these constraints in their ethics checklist.

## Prohibited uses

1. **Biometric profiling (including facial recognition)**  
   - Rationale: high risk of misidentification, surveillance harms, and disproportionate impact on vulnerable people.  
2. **Automated clinical or legal decision-making**  
   - Rationale: black-box decisions can cause harm, remove human judgement, and create liability.  
3. **Predictive risk scoring about individuals (without strong human oversight & consent)**  
   - Rationale: such models often encode bias and can stigmatise people; they may lead to unjust exclusion.  
4. **Training models on raw sensitive records without explicit, auditable consent**  
   - Rationale: training on survivor-authored or sensitive case files risks re-identification and breaches consent.  
5. **Publishing raw case data or evidence**  
   - Rationale: privacy and safety—do not expose PII, evidence registers, or chain-of-custody details publicly.

## Allowed approaches (with safeguards)

- **Accessibility assistance** (summaries, Easy-Read conversion, caption generation), *only* when:  
  - The required metadata is present (author, consent status), and  
  - Outputs are flagged as AI-generated and include provenance, and  
  - A mandatory human-review step is required before publication.

- **Retrieval-based systems (RAG)** used for augmenting summaries, if sources are auditable and provenance metadata is attached.

## Required mitigation steps for any AI feature

- Capture and store **consent metadata** that clearly states permitted uses.  
- Always mark AI outputs with source citation, model used, generation timestamp and human review status.  
- Provide an appeal or revision pathway for authors to correct or withdraw AI-generated outputs.  
- Prefer vendor-agnostic architectures and document fallback/export procedures.

Students must surface these boundaries in the ethics checklist and explain how their proposals enforce them.
