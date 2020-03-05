import csv

def get_rows(file):
    rows = []
    with open(file) as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            rows.append(row)
    return rows
    
filename = 'sample_products.csv'

items = get_rows(filename)
