# Find similar cells from column

import csv

with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)


# Find rows with similar values in a specific column
seen_comparisons = set()    # To keet track of comparisons already made
column_index = 0    # Compare second column

for i, row in enumerate(rows):
    for j, other_row in enumerate(rows[i + 1:], start = i + 1): # Start from the next row to avoid self-comparison
        if row[column_index] == other_row[column_index]:
            if (i, j) not in seen_comparisons and (j, i) not in seen_comparisons:
                print(f"Row {i} is similar to Row {j} based on column {column_index}") 