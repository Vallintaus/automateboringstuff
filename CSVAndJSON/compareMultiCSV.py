# Compare Data between multiple CSV files

import csv

def read_csv(filename):
    """Read a csv file and return a list of rows"""
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        return list(reader)
    
#Assuming we have 2 files ('file1.csv' 'file2.csv')
data1 = read_csv('example.csv')
data2 = read_csv('example2.csv')

# Find same rows that are in file1 and file2
common_rows = [row for row in data1 if row in data2]
print(f"Common rows: {common_rows}")


# show row indexes of similar rows
for i, row in enumerate(data1):
    if row in data2:
        j = data2.index(row) # Find index of the row in data2
        print(f"Common rows: File 1 -> Row {i} is same as File 2 -> Row {j}")
