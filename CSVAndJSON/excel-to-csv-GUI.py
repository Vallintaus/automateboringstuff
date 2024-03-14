import openpyxl
import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def convert_excel_to_csv(excel_file, csv_file):
    # Load the workbook, and select the active worksheet
    workbook = openpyxl.load_workbook(excel_file)
    sheet = workbook.active
    
    # Open the CSV file for writing
    with open(csv_file, 'w', newline="") as f:
        c = csv.writer(f)
        for r in sheet.rows:
            # Write each row to the CSV file
            c.writerow([cell.value for cell in r])

def select_excel_file():
    Tk().withdraw() # Prevents an empty tkinter window from appearing
    filename = askopenfilename(
        title="Select an Excel File",
        filetypes=[
            ("Excel Files", "*.xlsx"),
            ("Excel Macro-Enabled Files", "*.xlsm"),
            ("Excel Template Files", "*.xltx"),
            ("Excel Macro-Enabled Template Files", "*.xltm")
        ])
    return filename

def save_csv_file():
    Tk().withdraw() # Prevents an empty tkinter window from appearing
    # Show a "Save as" dialog box and return the path to the selected file
    filename = asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    return filename

if __name__ == "__main__":
    excel_file = select_excel_file()
    if excel_file: # Proceed if the user selected a file
        csv_file = save_csv_file()
        if csv_file: # Proceed if the user specified a file name
            convert_excel_to_csv(excel_file, csv_file)
            print("Conversion completed successfully!")
        else:
            print("CSV file save operation was cancelled.")
    else:
        print("Excel file selection was cancelled.")
