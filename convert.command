#!/bin/bash
cd "$(dirname "$0")" || exit 1

if ! command -v python3 >/dev/null 2>&1; then
    echo "python3 not found. Install Python 3, then try again."
    echo
    read -n 1 -s -r -p "Press any key to close..."
    exit 1
fi

python3 convert.py
status=$?

echo
if [ $status -eq 0 ]; then
    echo "Done. CSVs are in processed/"
else
    echo "Finished with errors (exit $status)."
fi

echo
read -n 1 -s -r -p "Press any key to close..." || true

exit $status
