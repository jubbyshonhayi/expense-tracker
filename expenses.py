import csv
from datetime import datetime
from utils import ensure_csv_exists, CSV_FILE

def add_expense():

    """Collect an expense from the user and save it to the CSV file."""

    ensure_csv_exists()

    date = datetime.now().strftime("%d-%m-%Y")

    category = input("Category: ").strip().title()

    while not category:
        print("Category can not be empty")
        category = input("Category: ").strip().title()

    description = input("Description: ").strip()

    while not description:
        print("description can not be empty!")
        description = input("Description: ").strip()
    
    while True:
        try:
            amount = float(input("Amount: "))
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            break

        except ValueError:
            print("Please enter a valid amount")
    
    try:
        with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, description, amount])
        print("Expense added successfully!")

    except OSError:
        print("Failed to add expense\n")


def view_expenses():

    try:
        print("\n=====EXPENSES=====\n")
        
        with open(CSV_FILE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            try:
                next(reader)
            except StopIteration:
                print("No expenses found.")
                return

            found_expenses = False

            print(f"{'Date':<12} {'Category':<15} {'Description':<30} {'Amount':>10}")
            print("-" * 70)
            
            for row in reader:

                if len(row) != 4: #handle a scenario where user(or even I) manually edited the csv
                    continue
                
                found_expenses = True

                print(f"{row[0]:<12} {row[1]:<15} {row[2]:<30} {float(row[3]):>10.2f}")

            if not found_expenses:
                print("No Expenses found.")

    except OSError:
        print("Error: Unable to read expenses.csv.")
