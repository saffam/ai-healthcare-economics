
from pathlib import Path
import pandas as pd

# Locate the main research repository.
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Input: the literature extraction spreadsheet saved as CSV.
INPUT_FILE = PROJECT_ROOT / "literature" / "literature_extraction.csv"

# Output: a summary table.
OUTPUT_DIR = PROJECT_ROOT / "results" / "tables"
OUTPUT_FILE = OUTPUT_DIR / "literature_summary.csv"

REQUIRED_COLUMNS = [
    "Study_ID",
    "Author",
    "Year",
    "Title",
    "Research_Question",
]


def main():
    if not INPUT_FILE.exists():
        print(f"Input file not found: {INPUT_FILE}")
        return

    data = pd.read_csv(INPUT_FILE)

    # Check that the expected columns are present.
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in data.columns
    ]

    if missing_columns:
        print("The literature extraction file is missing columns:")
        for column in missing_columns:
            print(f"- {column}")
        return

    # Remove rows that are entirely empty.
    data = data.dropna(how="all")

    if data.empty:
        print("No study records have been entered yet.")
        print("The analysis will run after genuine study records are added.")
        return

    # Identify incomplete records without inventing missing information.
    incomplete = data[
        data[REQUIRED_COLUMNS].isna().any(axis=1)
    ]

    print(f"Number of recorded study rows: {len(data)}")
    print(f"Number of incomplete records: {len(incomplete)}")

    # Count studies by research question.
    question_summary = (
        data["Research_Question"]
        .dropna()
        .value_counts()
        .rename_axis("Research_Question")
        .reset_index(name="Number_of_Studies")
    )

    # Count studies by publication year.
    year_summary = (
        data["Year"]
        .dropna()
        .astype(str)
        .value_counts()
        .rename_axis("Publication_Year")
        .reset_index(name="Number_of_Studies")
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    question_summary.to_csv(
        OUTPUT_DIR / "studies_by_research_question.csv",
        index=False
    )

    year_summary.to_csv(
        OUTPUT_DIR / "studies_by_year.csv",
        index=False
    )

    print("Summary tables have been created in results/tables/.")


if __name__ == "__main__":
    main()
