# xlsx-to-csv batch converter

Converts `.xlsx` files to CSV. Preserves folder structure. Handles multi-sheet workbooks.

## Setup

Requires Python 3 and `openpyxl`:

```
pip install openpyxl
```

## Usage

1. Drop `.xlsx` files (or folders of them) into `inbox/`
2. Run the script:

```
python3 convert.py
```

3. CSVs appear in `processed/`, mirroring the same folder structure from `inbox/`

## Multi-sheet workbooks

Each sheet becomes its own file:

- `report.xlsx` (sheets: Jan, Feb) → `report_Jan.csv`, `report_Feb.csv`
- `report.xlsx` (single sheet) → `report.csv`

## Notes

- Existing files in `processed/` are overwritten
- Legacy `.xls` files are not supported — `openpyxl` reads `.xlsx` only
