import csv
import os

CSV_FILE = "expenses.csv"

HEADERS = [
    "Date",
    "Category",
    "Description",
    "Amount"
]

def ensure_csv_exists():

    if not os.path.exists(CSV_FILE):
        try:
            with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(HEADERS)
                
        except OSError:
            print("Erro: Could not create the expenses.csv")
