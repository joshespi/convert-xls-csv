#!/usr/bin/env python3
import csv
import sys
from pathlib import Path
import openpyxl

INBOX = Path(__file__).parent / "inbox"
PROCESSED = Path(__file__).parent / "processed"


def convert_file(xlsx_path: Path, rel: Path) -> list[Path]:
    wb = openpyxl.load_workbook(xlsx_path, data_only=True)
    sheets = wb.sheetnames
    outputs = []

    for sheet_name in sheets:
        ws = wb[sheet_name]

        if len(sheets) == 1:
            out_name = rel.with_suffix(".csv")
        else:
            out_name = rel.with_name(f"{rel.stem}_{sheet_name}.csv")

        out_path = PROCESSED / out_name
        out_path.parent.mkdir(parents=True, exist_ok=True)

        with open(out_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            for row in ws.iter_rows(values_only=True):
                writer.writerow(["" if v is None else v for v in row])

        outputs.append(out_path)

    wb.close()
    return outputs


def main():
    if not INBOX.exists():
        print(f"inbox/ not found at {INBOX}")
        sys.exit(1)

    xlsx_files = sorted(
        p for p in INBOX.rglob("*") if p.suffix.lower() in {".xlsx", ".xls"}
    )

    if not xlsx_files:
        print("No .xlsx or .xls files found in inbox/")
        return

    total_files = 0
    total_sheets = 0
    errors = []

    for xlsx_path in xlsx_files:
        rel = xlsx_path.relative_to(INBOX)
        try:
            outputs = convert_file(xlsx_path, rel)
            for out in outputs:
                print(f"  OK  {rel} -> {out.relative_to(PROCESSED)}")
            total_sheets += len(outputs)
            total_files += 1
        except Exception as e:
            print(f"  ERR {rel}: {e}")
            errors.append((rel, e))

    print(f"\n{total_files} file(s), {total_sheets} sheet(s) converted.")
    if errors:
        print(f"{len(errors)} error(s).")
        sys.exit(1)


if __name__ == "__main__":
    main()
