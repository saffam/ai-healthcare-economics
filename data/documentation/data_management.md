# Research Data Management Plan

## 1. Purpose

This document describes how data used in the independent research project on the economics of artificial intelligence in healthcare will be obtained, stored, documented, processed and reported.

The objective is to maintain transparency, reproducibility and responsible data handling.

## 2. Data Sources

The project will prioritise:

- Publicly available government datasets.
- Official healthcare statistics.
- Published research datasets.
- Publicly available aggregate healthcare information.
- Official reports and policy publications.

Each source will be assessed individually before use.

## 3. Access and Reuse

Public accessibility does not automatically grant permission to redistribute or modify data.

Before using a dataset, the researcher will record:

- Dataset title.
- Publisher or responsible organisation.
- Original source URL.
- Date accessed.
- Licence or terms of use.
- Whether modification is permitted.
- Whether redistribution is permitted.
- Attribution requirements.
- Any restrictions or conditions.

Where reuse conditions are unclear, the data will not be redistributed until those conditions have been clarified.

## 4. Data Storage

Original data will be stored separately from processed data.

- Raw data will be retained in the local data/raw directory.
- Processed data will be stored in data/processed.
- Documentation will be stored in data/documentation.

Raw and processed datasets will not automatically be published to GitHub.

## 5. Data Protection

The project will not collect or use identifiable patient records.

It will not intentionally obtain confidential, restricted or unlawfully disclosed information.

Only data appropriate for independent secondary research will be considered.

## 6. Data Processing

All transformations will be documented.

Processing records should identify:

- Original dataset.
- Variables used.
- Excluded or missing observations.
- Cleaning procedures.
- Unit conversions.
- Any assumptions.
- Output file created.

Original source data will not be silently overwritten.

## 7. Data Quality

Data will be checked for:

- Missing values.
- Duplicate records.
- Inconsistent units.
- Incorrect data types.
- Unexpected values.
- Inconsistent dates or categories.
- Relevant changes in definitions over time.

Any limitations will be reported.

## 8. Publication

Only data that are appropriate for publication and whose reuse conditions have been checked will be considered for inclusion in the public repository.

Where redistribution is not permitted, the project may provide a source citation, description and reproducible processing instructions instead.

## 9. Limitations

The availability, quality and reuse conditions of healthcare datasets may vary.

The project will document these limitations rather than assume that every publicly accessible dataset is suitable for analysis.