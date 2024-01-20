# Etsy Sales Tax Condenser

This script processes CSV files containing Etsy sales data, extracting order information and creating corresponding output files. It also supports combining all monthly reports into a single file when run with the `-c` flag.

## Dependencies

- Regular expressions (Regex) support, provided by the `re` module.
- `pandas` for data manipulation and analysis.
- `argparse` for command-line option and argument parsing.

## Usage

1. Place your input CSV files in the "files" directory.
2. Run the script, and it will process all the CSV files found in the "files" directory.
3. The script will create corresponding output files in the "outputs" directory.
4. If you want to combine all the output files into a single file, run the script with the `-c` flag.

## How It Works

The script follows these main steps:

1. It searches for CSV files in the "files" directory.
2. For each input file, it reads and processes the data, extracting order information.
3. The script identifies order numbers, their amounts, taxes, and refund information.
4. It then creates output CSV files for each order with the desired headers in the "outputs" directory.
5. If the `-c` flag is used, the script combines all the output files into a single file named `combined.csv`.

## Handling Missing or Invalid Data

The script handles cases where the "Amount" and "Fees & Taxes" columns contain "--" (indicating missing or invalid data) by checking for these values before attempting to convert them to floats.

## Example Usage

Here are sample commands to run the script:

- To process the CSV files and create individual output files:

    ```
    python3 main.py
    ```

- To process the CSV files and combine all the output files into a single file:

    ```
    python3 main.py -c
    ```