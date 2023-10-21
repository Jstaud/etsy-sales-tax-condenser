import os
import csv
import re

# Function to extract the order number from the Title or Info field
def extract_order_number(row):
    title = row['Title']
    info = row['Info']
    match = re.search(r'Order #(\d+)', title + info)
    if match:
        return match.group(1)
    return ''

# Create the "outputs" directory if it doesn't exist
output_dir = 'outputs'
os.makedirs(output_dir, exist_ok=True)

# List all files in the "files" directory
input_dir = 'files'
input_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

for input_file in input_files:
    # Initialize an empty dictionary to store order information
    orders = {}

    # Read the input CSV file and process the data
    with open(os.path.join(input_dir, input_file), mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            order_number = extract_order_number(row)
            if order_number:
                if order_number not in orders:
                    orders[order_number] = {
                        'Order #': order_number,
                        'Amount': '',
                        'Taxes': 0,
                        'Refunded?': 'No'
                    }
                if row['Type'] == 'Sale':
                    orders[order_number]['Amount'] = row['Amount']
                elif row['Type'] == 'Tax':
                    amount = row['Fees & Taxes'].replace('$', '').replace(',', '')
                    if amount != '--':
                        orders[order_number]['Taxes'] += float(amount)
                elif row['Type'] == 'Refund':
                    orders[order_number]['Refunded?'] = 'Yes'

    # Write the processed data to a new CSV file in the "outputs" directory
    output_file = os.path.join(output_dir, f'output_{input_file}')
    with open(output_file, mode='w', newline='') as file:
        fieldnames = ["Order #", "Amount", "Taxes", "Refunded?"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for order in orders.values():
            writer.writerow(order)
