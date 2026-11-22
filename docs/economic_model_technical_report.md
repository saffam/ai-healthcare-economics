# Economic Model Technical Report

## 1. Purpose

This document describes the technical design, inputs, calculations, assumptions and validation procedures used in the economic analysis of AI-assisted diabetic retinopathy screening.

The purpose of the model is to examine the potential economic consequences of introducing AI-assisted screening into an existing diabetic eye screening pathway.

The model is intended to support transparent economic reasoning. It is not a clinical decision-making tool and does not independently establish the safety, effectiveness or cost-effectiveness of an AI system.

## 2. Research question

Under what clinical, economic and organisational conditions could AI-assisted diabetic retinopathy screening provide economic value within an NHS screening pathway?

## 3. Analytical perspective

The primary analytical perspective is the NHS and personal social services perspective, where the available evidence permits.

Relevant costs may include:

- Screening service costs.
- AI software and licensing costs.
- Hardware and infrastructure.
- IT integration.
- Staff training.
- Clinical review and referral.
- Maintenance and monitoring.
- Additional investigations and follow-up.

Wider societal consequences may be discussed separately where evidence is available. They must not be combined with NHS costs without clearly identifying the change in perspective.

## 4. Comparators

The analysis distinguishes between:

1. Existing screening without AI.
2. AI-assisted screening with human clinical oversight.
3. Autonomous AI screening, where the available evidence supports its separate evaluation.

These approaches must not be treated as interchangeable. Their clinical responsibilities, staffing requirements, implementation costs and regulatory requirements may differ.

## 5. Model population

The intended population is people eligible for diabetic eye screening within the relevant NHS screening pathway.

The model population must be defined using the population represented by the available evidence. National screening activity figures must not automatically be interpreted as the number of people eligible for an AI intervention.

## 6. Model inputs

Model inputs may include:

- Eligible population.
- Screening attendance.
- Screening coverage.
- Image gradability.
- Diagnostic sensitivity.
- Diagnostic specificity.
- Referral rates.
- Repeat screening requirements.
- Staff time.
- Screening costs.
- AI implementation costs.
- Maintenance costs.
- Follow-up costs.

Every numerical input must have a documented source, unit, reference year and evidence classification.

## 7. Evidence classifications

Inputs must be classified as one of the following:

**Published empirical evidence:** A value directly reported by an identified study or official dataset.

**Published model estimate:** A value estimated by an existing economic or clinical model.

**Derived value:** A value calculated transparently from published evidence.

**Illustrative assumption:** A value used to demonstrate a possible scenario where empirical evidence is unavailable.

**Unavailable:** A value for which sufficiently reliable evidence has not been identified.

Illustrative assumptions must never be presented as observed NHS data.

## 8. Economic calculations

Where the available inputs permit, the model may calculate:

- Total screening pathway costs.
- AI implementation and operating costs.
- Cost differences between pathways.
- Differences in screening and referral activity.
- Cost per person screened.
- Cost per additional person appropriately identified.
- Incremental cost-effectiveness measures, where valid outcome and comparator data are available.

The calculation method and underlying inputs must be documented for each reported outcome.

An incremental cost-effectiveness ratio must not be calculated when the relevant incremental costs and health outcomes are not sufficiently supported.

## 9. Clinical outcomes

Clinical outcomes may include:

- Detection of referable diabetic retinopathy.
- Missed cases.
- False-positive referrals.
- False-negative results.
- Additional clinical assessments.
- Timeliness of referral and follow-up.

Diagnostic accuracy is not equivalent to improved patient health. Any claim about improved visual outcomes requires appropriate outcome evidence.

## 10. Uncertainty

Uncertainty may arise from:

- Differences between study populations.
- Differences between AI systems.
- Differences in screening pathways.
- Uncertain cost estimates.
- Missing implementation costs.
- Variation in diagnostic performance.
- Changes in screening attendance.
- Differences between international and NHS settings.

Sensitivity and scenario analyses should be conducted only using documented parameter values and defensible ranges.

## 11. Model validation

The model should be checked for:

- Missing inputs.
- Invalid values.
- Incorrect units.
- Duplicate parameters.
- Inconsistent definitions.
- Arithmetic errors.
- Unsupported assumptions.
- Implausible outputs.

Validation checks do not prove that the model accurately represents real-world clinical practice. They establish that its documented calculations and inputs meet specified technical checks.

## 12. Limitations

The model is dependent on the availability and quality of published evidence.

International economic estimates may not transfer directly to the NHS because of differences in healthcare costs, clinical pathways, staffing, technology procurement, screening organisation and reimbursement.

Where the available evidence is insufficient, the model must report the limitation rather than manufacture a numerical estimate.

## 13. Reproducibility

The model's inputs, source references, scripts, validation procedures and outputs should be documented within the project repository.

Restricted, identifiable or otherwise inappropriate data must not be uploaded to the public repository.

## 14. Interpretation

The model should be interpreted as an evidence-informed economic analysis rather than proof that AI screening is universally beneficial.

The conclusions should reflect the quality of the evidence, the uncertainty of the inputs and the applicability of the findings to the NHS.