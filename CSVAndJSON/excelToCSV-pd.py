# excel to CSV converter using pandas

import pandas as pd

def excel_to_csv(excel_file_path, csv_file_path, sheet_name = 0):
    """
    Converts an Excel file to a CSV file.

    Parameters:
    - excel_file_path: Path to the Excel file.
    - csv_file_path: Path where the CSV file will be saved.
    - sheet_name: Sheet to convert. By default, the first sheet is converted.
    """
    # read excel file
    ef = pd.read_excel(excel_file_path, sheet_name=sheet_name)

    # Write to CSV file
    ef.to_csv(csv_file_path, index=False)


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage: python excelToCSV.py <ExcelFilePath> <CSVFilePath>")
    else:
        excel_file_path = sys.argv[1]
        csv_file_path = sys.argv[2]
        excel_to_csv(excel_file_path, csv_file_path)