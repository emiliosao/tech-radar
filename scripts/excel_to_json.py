import pandas as pd
import json
import sys

# Usage: python excel_to_json.py 2025-03
if len(sys.argv) != 2:
    print("Usage: python excel_to_json.py <sheet_name>")
    sys.exit(1)

sheet_name = sys.argv[1]
xlsx_filename = "./data/radar_entries.xlsx"
json_filename = f"./data/radar.json"

# Load Excel and read the specified sheet
df = pd.read_excel(xlsx_filename, sheet_name=sheet_name)

# Normalize columns and clean up
df = df.rename(columns=lambda x: x.strip().lower())
df = df.where(pd.notna(df), "")  # Replace NaNs with empty strings

# Build the JSON
json_data = {
    "date": sheet_name,
    "entries": df[["label", "quadrant", "ring", "link", "moved"]].to_dict(orient="records")
}

# Write to file
with open(json_filename, "w") as f:
    json.dump(json_data, f, indent=2)

print(f"JSON file saved to {json_filename}")
