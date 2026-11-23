# Research File Audit

**Project:** The Economics of Artificial Intelligence in Healthcare: Economic Value, Human Trust, Institutional Differences and the Governance of AI-Assisted Decision-Making

**Audit type:** Independent project documentation and consistency audit  
**Status:** Initial audit — pending final file-by-file verification  
**Date:** 23 November 2026

## 1. Purpose

This audit establishes a structured record of the project's research files, identifies areas requiring verification, and checks whether the documentation supports the central research question and six subsidiary research questions.

The audit is intended to improve consistency, traceability, transparency and reproducibility before the final manuscript is prepared.

This is an internal research-quality exercise. It is not an external peer review, institutional audit or formal certification.

## 2. Research question coverage

| Research question | Subject | Required evidence and documentation |
|---|---|---|
| RQ1 | Economic value | Economic evaluations, productivity evidence, clinical outcomes and cost-effectiveness studies |
| RQ2 | Costs | Technology, implementation, training, maintenance, monitoring and opportunity costs |
| RQ3 | Workforce and human judgement | Professional autonomy, workflow, productivity and clinical responsibility |
| RQ4 | Human trust | Healthcare professional and patient trust, transparency, reliability and oversight |
| RQ5 | Institutional differences | Organisational capacity, infrastructure, population characteristics and healthcare-system context |
| RQ6 | Policy and governance | Regulation, reimbursement, accountability, equity and institutional governance |

**Audit assessment:** All six research questions have corresponding analytical documentation according to the project's development record. Their final evidence coverage must be checked against the completed literature extraction and manuscript.

## 3. Research protocol and methods

The following documents should be maintained as the authoritative methodological record:

| File | Audit requirement |
|---|---|
| `docs/research_questions.md` | Confirm consistency with the approved research question |
| `docs/research_objectives.md` | Confirm objectives correspond to all six research questions |
| `docs/research_protocol.md` | Confirm search, screening, extraction and synthesis procedures are documented |
| `docs/literature_search_strategy.md` | Confirm databases, search dates and search terms are recorded |
| `docs/literature_screening_criteria.md` | Confirm inclusion and exclusion criteria are explicit |
| `literature/quality_assessment.md` | Confirm study appraisal procedures and limitations are documented |
| `docs/reproducibility_record.md` | Confirm analytical procedures and software are recorded |

The actual existence, completeness and internal consistency of each file must be confirmed before the audit is marked final.

## 4. Literature and evidence records

The following registers form the project's evidence-tracking system:

| File | Required verification |
|---|---|
| `literature/source_register.csv` | Every included source has a unique identifier and bibliographic details |
| `literature/literature_extraction.csv` | Extracted findings correspond to the cited publications |
| `literature/case_study_source_register.csv` | Diabetic retinopathy sources are traceable |
| `literature/case_study_extraction.csv` | Study characteristics and findings are supported by source material |
| `literature/case_study_quality_appraisal.md` | Appraisal reflects study design and limitations |
| `literature/uk_case_study_source_register.csv` | UK and NHS evidence is distinguished from international evidence |
| `literature/diagnostic_accuracy_source_register.csv` | Diagnostic accuracy sources are identifiable |
| `literature/diagnostic_accuracy_extraction.csv` | Accuracy estimates are checked against the original studies |
| `literature/clinical_evidence_gaps.csv` | Unresolved clinical evidence is documented |

### Required evidence checks

For each source, verify:

1. The publication exists.
2. The authors, title, year and publication details are correct.
3. The DOI or official URL resolves to the intended source.
4. The study design and population are accurately described.
5. Extracted numerical findings agree with the original publication.
6. The interpretation does not exceed the evidence.
7. Conflicts of interest and relevant limitations are recorded.
8. The source is appropriate for the geographical and institutional context in which it is used.

Abstract-level information must not be presented as if full-text extraction had been completed.

## 5. NHS diabetic retinopathy case study

The case study requires a clear distinction between the NHS screening pathway and evidence obtained from international AI screening studies.

Files requiring final consistency checks include:

- `docs/case_study_scope.md`
- `docs/nhs_diabetic_eye_screening_pathway.md`
- `data/documentation/nhs_screening_pathway.csv`
- `data/processed/nhs_screening_coverage.csv`
- `data/documentation/nhs_screening_coverage_notes.md`
- `docs/case_study_economic_model.md`
- `data/documentation/case_study_parameter_register.csv`
- `data/documentation/case_study_parameter_sources.md`
- `data/documentation/nhs_cost_data_strategy.md`
- `data/documentation/nhs_cost_extraction.csv`
- `data/documentation/cost_evidence_gaps.csv`
- `docs/economic_outcome_definitions.md`

### Specific audit requirements

- Screening coverage must not be interpreted as an effect of AI.
- Diagnostic sensitivity and specificity must be linked to the relevant population, disease threshold and screening conditions.
- International estimates must not automatically be treated as NHS estimates.
- Screening attendance, image gradability, referral and follow-up must be treated as distinct outcomes.
- Cost definitions must be consistent across the pathway.
- Any rounded or approximate descriptive data must be labelled appropriately.
- Unverified values must not be used as established model inputs.

## 6. Economic analysis files

The economic analysis documentation includes:

- `docs/quantitative_analysis_plan.md`
- `docs/economic_model_technical_report.md`
- `docs/missing_economic_data_impact_analysis.md`
- `docs/economic_uncertainty_analysis.md` (if present)
- `data/processed/case_study_model_inputs.csv`
- `src/case_study_model.py`
- `src/validate_case_study_data.py`
- `src/validate_economic_calculations.py`
- `src/run_case_study_economic_model.py`

The current model readiness assessment identifies 16 parameters, of which zero are ready and 16 remain unresolved.

The report is generated at:

`results/tables/case_study_model_readiness.csv`

This is an appropriate record of the current evidence limitations. It must not be described as a completed cost-effectiveness analysis.

### Economic audit requirements

- Confirm that cost and outcome definitions are explicit.
- Check calculations against independently reproducible test cases.
- Confirm that units are consistent.
- Distinguish one-off and recurring costs.
- Distinguish average and incremental costs.
- Document the perspective and time horizon.
- Document uncertainty and missing inputs.
- Avoid presenting illustrative values as observed NHS expenditure.
- Do not calculate or report an incremental cost-effectiveness ratio when required inputs or outcomes are unavailable.

## 7. Analytical documentation

The following topic-specific analyses should be reconciled with the manuscript:

- Screening attendance economic analysis.
- Diagnostic errors and referral analysis.
- Diagnostic accuracy versus economic value.
- Workforce productivity analysis.
- Human trust and clinical judgement analysis.
- Institutional differences analysis.
- Reimbursement and regulation analysis.
- Equity and distributional analysis.
- AI-assisted versus autonomous screening analysis.

Each analytical document should identify its evidence base, principal arguments, limitations and relationship to the research questions.

Repeated arguments should be consolidated in the manuscript rather than reproduced unnecessarily.

## 8. Manuscript consistency

The authoritative manuscript file is:

`manuscript/manuscript_draft.md`

The final manuscript must be consistent with the research protocol, evidence registers, economic analysis and verified references.

The following checks are required:

1. The title accurately reflects the research scope.
2. The abstract does not claim findings that have not been established.
3. The introduction explains the research problem and objectives.
4. The literature review accurately represents the available evidence.
5. The methodology describes the work actually performed.
6. The results distinguish evidence synthesis from illustrative analysis.
7. The discussion recognises contradictory evidence and uncertainty.
8. Recommendations follow from the evidence.
9. Limitations are explicit.
10. All references are traceable and correctly attributed.

The manuscript must not claim NHS endorsement, university affiliation, formal ethics approval, peer review or clinical validation.

## 9. Data management and reproducibility

The following files should be checked:

- `data/documentation/data_management.md`
- `data/documentation/data_dictionary.md`
- `data/documentation/dataset_register.csv`
- `requirements.txt`
- `.gitignore`

The audit should confirm that:

- Data sources and transformations are documented.
- Raw or restricted data are not unintentionally committed.
- Generated outputs can be reproduced from documented scripts.
- Software dependencies are recorded.
- File paths are relative to the project repository where practicable.
- No confidential or identifiable patient information is included.

## 10. Outstanding audit actions

| Priority | Action | Completion condition |
|---|---|---|
| High | Verify all references | Bibliographic records checked against original sources |
| High | Verify extracted numerical results | Values checked against full-text publications where available |
| High | Reconcile research questions and manuscript | All six questions are addressed accurately |
| High | Review economic model inputs | Every value has an appropriate source and status |
| High | Review NHS cost evidence | Cost definitions, periods and populations are comparable |
| Medium | Check all analytical documents | Consistent terminology and no unsupported duplication |
| Medium | Re-run validation scripts | Successful execution documented |
| Medium | Check repository data management | No restricted or confidential material committed |
| Medium | Review citations and copyright | Attribution and reuse requirements addressed |
| Final | Complete manuscript audit | All sections and references reconciled |

## 11. Audit conclusion

The project has developed a substantial methodological, analytical and documentary foundation covering the economic, clinical, workforce, trust, institutional, equity and governance dimensions of healthcare AI.

The economic model readiness assessment has successfully identified the outstanding input requirements. It currently reports 16 unresolved parameters, so no defensible real-world NHS cost-effectiveness result can yet be reported.

The next priority is verification of the original literature and NHS evidence, followed by reconciliation of the evidence registers and manuscript.

This audit remains provisional until the individual files and source records have been inspected and the outstanding actions have been completed.

**Research status:** Independent secondary research in progress.

**Interpretation:** No definitive conclusion that AI-assisted diabetic retinopathy screening is cost-effective in NHS England is established by the current model.