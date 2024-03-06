# Adds blank rows to spreadsheet. Arguments N = starting row, M = number of blank rows, filename = filename


import openpyxl
import sys

def insert_blank_rows(start_row, num_rows, filename):
    wb = openpyxl.load_workbook(filename)
    ws = wb.active

    # Insert blank rows starting from start_row. --> if idx = 2 --> row 2 will be blank and original row 2 will be moved down
    ws.insert_rows(idx = start_row, amount = num_rows)

    new_filename = 'modified' + filename
    wb.save(new_filename)
    print(f"Inserted {num_rows} blank row(s) starting from row {start_row} in '{new_filename}'")

if __name__ == '__main__':
    if len(sys.argv) == 4:
        try:
            N = int(sys.argv[1])
            M = int(sys.argv[2])
            filename = sys.argv[3]
            insert_blank_rows(N, M, filename)
        except ValueError:
            print("Please make sure N and M are valid integers.")
        except FileNotFoundError:
            print(f"File '{filename}' not found. Please make sure the file exists.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Usage: python blankRowInserter.py N M filename")            