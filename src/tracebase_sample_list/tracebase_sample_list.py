#!/usr/bin/env python
from __future__ import annotations

import argparse
from collections.abc import Sequence
from pathlib import Path

import pandas as pd


def headers(file: Path) -> Sequence[str]:
    column_headers = []
    suffix = file.suffix.lower()
    if suffix == ".xlsx":
        excel_file = pd.ExcelFile(file)
        # Skip Excel files that look like the Animals and Samples table
        if "Animals" not in excel_file.sheet_names:
            column_headers = excel_file.parse(
                nrows=1,
                header=None,
                sheet_name=0,
                engine="openpyxl",
            ).iloc[0]
    elif suffix == ".csv":
        column_headers = pd.read_csv(
            file,
            nrows=1,
            header=None,
        ).iloc[0]
    elif suffix == ".tsv":
        # column_headers = "TSV"
        pass
    return column_headers


def sample_names(file: Path) -> Sequence[str]:
    # Known nonsample column names in AccuCor and Isocor files
    nonsample_column_names = [
        "label",  # Accucor format
        "metaGroupId",
        "groupId",
        "goodPeakCount",
        "medMz",
        "medRt",
        "maxQuality",
        "isotopeLabel",
        "compound",
        "compoundId",
        "formula",
        "expectedRtDiff",
        "ppmDiff",
        "parent",
        "Compound",
        "adductName",
    ]
    # Get column headings from file
    column_headers = headers(file)

    # Remove known nonsample column names
    sample_name_columns = [
        colname for colname in column_headers if colname not in nonsample_column_names
    ]

    # Remove *_Label columns in accucor corrected sheets
    sample_name_columns = [
        colname for colname in sample_name_columns if not colname.endswith("_Label")
    ]

    return sample_name_columns


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "directory", type=Path, help="Path to directory of AccuCor files"
    )
    args = parser.parse_args(argv)

    directory: Path = args.directory

    files: list[Path] = [f for f in directory.iterdir() if f.is_file()]
    for file in sorted(files):
        for sample in sample_names(file):
            print(f"{file.name}\t{sample}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
