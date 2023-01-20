# Tracebase Sample List

A simple tool that lists the samples in all of the AccuCor or Isocor files in a directory.

The intended use is to quickly get a list of all of the samples from all of the
peak data files in a given directory to simplify filling out a sample sheet for
Tracebase.

## Install

```bash
pip install git+https://github.com/lparsons/tracebase-sample-list.git
```

## Usage

```bash
tracebase-sample-list /path/to/accucor/files
```

## Output

Output to STDOUT a tab delimited list with `filename` and `sample_name`.

Only `.xlsx`, `.csv.` and `.tsv` files are considered.
