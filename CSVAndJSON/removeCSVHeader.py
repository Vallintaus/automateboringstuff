# This program will remove the header/first row from CSV Files

import csv
import os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working directory
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue    # Skip non csv files
    print("Removing header from " + csvFilename + '...')

    # Read the CSV file in (skip first row)
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue    # Skip first row
        csvRows.append(row)
    csvFileObj.close()

    # Write out the CSV file
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()