"""Plot approximate NHS diabetic eye screening coverage."""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]

DATA_FILE = ROOT / "data" / "processed" / "nhs_screening_coverage.csv"
OUTPUT_DIR = ROOT / "results" / "figures"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

data = pd.read_csv(DATA_FILE)

required_columns = {"year", "coverage_percent"}

if not required_columns.issubset(data.columns):
    raise ValueError("The coverage dataset is missing required columns.")

data = data.sort_values("year")

fig, ax = plt.subplots(figsize=(9, 5))

ax.plot(
    data["year"],
    data["coverage_percent"],
    marker="o"
)

ax.set_title("Approximate diabetic eye screening coverage in England")
ax.set_xlabel("Year")
ax.set_ylabel("Coverage (%)")
ax.set_ylim(0, 100)
ax.grid(True, alpha=0.3)

fig.tight_layout()

output_file = OUTPUT_DIR / "nhs_screening_coverage.png"
fig.savefig(output_file, dpi=300)

print(f"Chart saved to: {output_file}")