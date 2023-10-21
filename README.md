# etsy-sales-tax-condenser
A tool for extracting total sales tax paid and total sales elgible for sales taxes from Etsy monthly exports.
# Order Data Processing Script

This Python script is designed to process CSV files containing order data. It extracts order numbers, amounts, taxes, and refund information from the input files and generates output files with specific headers. The script can handle multiple input files located in the "files" directory and outputs the results in the "outputs" directory. This is used primarily for reporting quarterly sales taxes.

## Prerequisites

Before using this script, ensure that you have the following prerequisites in place:

- Python 3.x installed on your system.
- The `csv` module, which is part of the Python standard library.
- The `os` module, which is part of the Python standard library.
- Regular expressions (Regex) support, provided by the `re` module.

## Usage

1. Place your input CSV files in the "files" directory.
2. Run the script, and it will process all the CSV files found in the "files" directory.
3. The script will create corresponding output files in the "outputs" directory.

## How It Works

The script follows these main steps:

1. It searches for CSV files in the "files" directory.
2. For each input file, it reads and processes the data, extracting order information.
3. The script identifies order numbers, their amounts, taxes, and refund information.
4. It then creates output CSV files for each order with the desired headers in the "outputs" directory.

## Handling Missing or Invalid Data

The script handles cases where the "Amount" and "Fees & Taxes" columns contain "--" (indicating missing or invalid data) by checking for these values before attempting to convert them to floats.

## Example Usage

Here is a sample command to run the script:

```
python3 main.py
```