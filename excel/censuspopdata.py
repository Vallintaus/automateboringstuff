import os
import openpyxl
import pprint

current_dir = os.getcwd()
file_path = os.path.join(current_dir, 'excel', 'censuspopdata.xlsx')

wb = openpyxl.load_workbook(file_path)
sheet = wb['Population by Census Tract']
countyData = {}

print("Reading rows....")

for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract.
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += int(pop)

print('Writing results....')

output_file_path = os.path.join(current_dir, 'census2010.py')
with open(output_file_path, 'w') as resultFile:
    resultFile.write('allData = ' + pprint.pformat(countyData))
print('Done')