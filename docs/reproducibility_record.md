# Research Reproducibility Record

## 1. Project

The Economics of Artificial Intelligence in Healthcare.

## 2. Case study

AI-assisted diabetic retinopathy screening.

## 3. Software

- Python
- pandas
- matplotlib
- openpyxl
- Visual Studio Code
- Git and GitHub Desktop

## 4. Main data files

- `data/processed/nhs_screening_coverage.csv`
- `data/documentation/case_study_parameter_register.csv`
- `data/documentation/nhs_screening_pathway.csv`
- `literature/diagnostic_accuracy_extraction.csv`
- `data/documentation/nhs_cost_extraction.csv`

## 5. Main scripts

- `src/analyse_literature.py`
- `src/case_study_model.py`
- `src/plot_nhs_screening_coverage.py`
- `src/validate_case_study_data.py`

## 6. Reproduction instructions

Activate the project virtual environment.

Run:

`python src/plot_nhs_screening_coverage.py`

Then run:

`python src/validate_case_study_data.py`

The economic model must not be treated as producing empirical results until the required cost, clinical and pathway inputs have been sourced and verified.

## 7. Data provenance

Each dataset must have an accompanying source record and a description of its measurement definition.

## 8. Data restrictions

Do not commit identifiable patient data, restricted datasets, confidential procurement documents or material that cannot lawfully be redistributed.

## 9. Limitations

The current screening coverage dataset contains approximate values. The economic parameter register contains unresolved evidence gaps. The present code checks data readiness and creates descriptive output; it does not yet establish NHS cost-effectiveness.

## 10. Version control

Research documents, source registers, code and permitted derived datasets are version controlled through Git.

Changes should be committed with meaningful descriptions.
