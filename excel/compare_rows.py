import openpyxl
from collections import Counter


def compare_data(file_path, column):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active

    data = [sheet[f"{column}{row}"].value for row in range(1, sheet.max_row + 1) if sheet[f"{column}{row}"].value is not None]

    data_count = Counter(data)

    unique_entries = [item for item, count in data_count.items() if count == 1]
    duplicate_entries = {item: count for item, count in data_count.items() if count > 1}

    return unique_entries, duplicate_entries

def main():
    file_path = 'example.xlsx'
    column = 'A'
    unique_entries, duplicate_entries = compare_data(file_path, column)

    print("Unique entries: ")
    for entry in unique_entries:
        print(entry)

    print("\nDuplicate Entries: ")
    for entry, count in duplicate_entries.items():
        print(f"{entry}: {count} times")

if __name__ == "__main__":
    main()