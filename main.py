import csv
import os

# Function to calculate totals for a given CSV file
def calculate_totals(input_file, output_file):
    total_sales_taxes_paid = 0
    total_taxable_sales = 0

    with open(input_file, newline='') as input_csvfile:
        reader = csv.DictReader(input_csvfile)
        
        for row in reader:
            date = row['Date']
            type = row['Type']
            currency = row['Currency']
            amount = row['Amount']
            fees_taxes = row['Fees & Taxes']

            if type == 'Sale' and currency == 'USD':
                total_taxable_sales += float(amount.replace('$', '').replace(',', ''))

            if type == 'Tax' and currency == 'USD':
                total_sales_taxes_paid += float(fees_taxes.replace('$', '').replace(',', ''))

    # Write the calculated totals to the output file
    with open(output_file, 'w', newline='') as output_csvfile:
        fieldnames = ['Type', 'Amount']
        writer = csv.DictWriter(output_csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Type': 'Total Sales Taxes Paid', 'Amount': f'${total_sales_taxes_paid:.2f}'})
        writer.writerow({'Type': 'Total Taxable Sales', 'Amount': f'${total_taxable_sales:.2f}'})

# Directory containing CSV files
directory_path = '/files'

# List all CSV files matching the filename format
csv_files = [file for file in os.listdir(directory_path) if file.startswith('etsy_statement_') and file.endswith('.csv')]

# Iterate through the CSV files, calculate totals, and generate output files
for csv_file in csv_files:
    input_csv_path = os.path.join(directory_path, csv_file)
    output_csv_path = os.path.join(directory_path, f"{csv_file.replace('.csv', '_output.csv')}")
    
    calculate_totals(input_csv_path, output_csv_path)
    print(f'Output file created: {output_csv_path}')
