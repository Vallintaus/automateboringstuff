# This will get all phone numbers and "clean" them to some default form

import openpyxl
import re

#load workbook
wb = openpyxl.load_workbook('contacts.xlsx')
sheet = wb.active

# Regex patter
phone_pattern = re.compile(r'(\d{3})[-,\s]?(\d{3})[-,\s]?(\d{4})')

# Iterate ove the row in column B
for row in range(4, sheet.max_row + 1):
    cell = sheet[f'B{row}']
    if cell.value:
        # Search for phone number pattern in cell
        match = phone_pattern.search(str(cell.value))
        if match:
            standardized_phone = f"{match.group(1)} {match.group(2)} {match.group(3)}"
            cell.value = standardized_phone

wb.save('cleaned_contacts.xlsx')
