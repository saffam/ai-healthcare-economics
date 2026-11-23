
"""Check readiness of the diabetic retinopathy economic model.

This script checks whether required inputs are present and verified.
It does not calculate or claim real-world NHS cost-effectiveness.
"""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = ROOT / "data" / "processed" / "case_study_model_inputs.csv"
OUTPUT_FILE = ROOT / "results" / "tables" / "case_study_model_readiness.csv"

REQUIRED_COLUMNS = [
    "parameter_id",
    "parameter_name",
    "value",
    "unit",
    "evidence_source",
    "evidence_status",
    "notes",
]

ACCEPTED_STATUSES = {
    "verified",
    "provisional",
    "missing",
    "excluded",
    "not_applicable",
}


def main():
    print("Checking diabetic retinopathy economic model readiness...")
    print("This is an input-readiness check, not a cost-effectiveness analysis.")
    print()

    if not INPUT_FILE.exists():
        print(f"ERROR: Input file not found: {INPUT_FILE}")
        return 1

    with INPUT_FILE.open(
        "r", newline="", encoding="utf-8-sig"
    ) as file:
        nonblank_lines = (line for line in file if line.strip())
        reader = csv.DictReader(nonblank_lines)

        if reader.fieldnames != REQUIRED_COLUMNS:
            print("ERROR: CSV headings do not match the required structure.")
            print("Found:", reader.fieldnames)
            print("Expected:", REQUIRED_COLUMNS)
            return 1

        rows = list(reader)

    report = []
    seen_ids = set()

    for row in rows:
        parameter_id = (row.get("parameter_id") or "").strip()
        parameter_name = (row.get("parameter_name") or "").strip()
        value = (row.get("value") or "").strip()
        unit = (row.get("unit") or "").strip()
        evidence_source = (row.get("evidence_source") or "").strip()
        evidence_status = (row.get("evidence_status") or "").strip().lower()
        notes = (row.get("notes") or "").strip()

        issues = []

        if not parameter_id:
            issues.append("Missing parameter ID")
        elif parameter_id in seen_ids:
            issues.append("Duplicate parameter ID")

        seen_ids.add(parameter_id)

        if not parameter_name:
            issues.append("Missing parameter name")
        if not unit:
            issues.append("Missing unit")
        if not value:
            issues.append("Missing value")
        if not evidence_source:
            issues.append("Missing evidence source")
        if not evidence_status:
            issues.append("Missing evidence status")
        elif evidence_status not in ACCEPTED_STATUSES:
            issues.append("Unrecognised evidence status")
        if evidence_status != "verified":
            issues.append("Input is not marked as verified")
        if not notes:
            issues.append("Missing explanatory notes")

        readiness = "ready" if not issues else "unresolved"

        report.append({
            "parameter_id": parameter_id,
            "parameter_name": parameter_name,
            "value": value,
            "unit": unit,
            "evidence_source": evidence_source,
            "evidence_status": evidence_status,
            "readiness": readiness,
            "issues": "; ".join(issues),
        })

    expected_ids = {f"P{i:03d}" for i in range(1, 17)}
    actual_ids = {
        (row.get("parameter_id") or "").strip()
        for row in rows
    }
    missing_ids = sorted(expected_ids - actual_ids)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    output_columns = [
        "parameter_id",
        "parameter_name",
        "value",
        "unit",
        "evidence_source",
        "evidence_status",
        "readiness",
        "issues",
    ]

    with OUTPUT_FILE.open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=output_columns)
        writer.writeheader()
        writer.writerows(report)

    ready_count = sum(
        row["readiness"] == "ready" for row in report
    )
    unresolved_count = len(report) - ready_count

    print(f"Input parameters found: {len(rows)}")
    print(f"Ready parameters: {ready_count}")
    print(f"Unresolved parameters: {unresolved_count}")

    if missing_ids:
        print("Parameter IDs not found:", ", ".join(missing_ids))

    print()
    print("Readiness report created:")
    print(OUTPUT_FILE.relative_to(ROOT))
    print()

    if unresolved_count:
        print("MODEL STATUS: NOT READY")
        print("Do not calculate or report real-world NHS cost-effectiveness.")
    else:
        print("MODEL STATUS: INPUTS MARKED READY")
        print("Independent evidence and model validation are still required.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
