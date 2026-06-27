import csv
from datetime import datetime
from utils import  CSV_FILE

# View all recorded expenses
def view_expenses():
    """Display all recorded expenses."""

    TABLE_WIDTH = 75
    expenses = []

    try:
        with open(CSV_FILE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            # Skip the header row
            try:
                next(reader)

            except StopIteration:
                print("No expenses found.")
                return

            for row in reader:

                # Skip malformed rows (e.g., manually edited CSV)
                if len(row) != 4:
                    continue
                
                expenses.append(row)

        if not expenses:
            print("No expenses found.")
            return

        # Print report headers
        print("=" * TABLE_WIDTH)
        print("ALL EXPENSES".center(TABLE_WIDTH))
        print("=" * TABLE_WIDTH)
        print(f"Total Expenses: {len(expenses)}\n")

        print(f"{'Date':<12} {'Category':<15} {'Description':<35} {'Amount':>10}")
        print("-" * TABLE_WIDTH)

        for row in expenses:
            print(f"{row[0]:<12} {row[1]:<15} {row[2]:<35} {float(row[3]):>10.2f}")

        print()

        # Calculate the total amount of all recorded expenses
        grand_total = sum(float(row[3]) for row in expenses)

        print("-" * TABLE_WIDTH)
        print(f"{'TOTAL':<64} {grand_total:>11.2f}")
        print("-" * TABLE_WIDTH)

    except OSError:
        print("Error: Unable to read expenses.csv.")


# View expenses grouped by category
def category_summary():

    """Display the total amount spent in each category."""

    TABLE_WIDTH = 30
    totals = {}

    try:

        with open(CSV_FILE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            # Skip the header row
            try:
                next(reader)

            except StopIteration:
                print("No expenses found.")
                return
            
            for row in reader:

                # Skip malformed rows (e.g., manually edited CSV)
                if len(row) != 4:
                    continue

                # Store category and amount
                category = row[1]
                amount = float(row[3])

                if category in totals:
                    totals[category] += amount

                else:
                    totals[category] = amount

        if not totals:
            print("No categories found.")
            return
        
        # Print report headers
        print("=" * TABLE_WIDTH)
        print("CATEGORY SUMMARY".center(TABLE_WIDTH))
        print("=" * TABLE_WIDTH)
        print(f"\nTotal Categories: {len(totals)}\n")
        print(f"{'Category':<20} {'Amount':>10}")
        print("-" * TABLE_WIDTH)

        for category, total in sorted(totals.items()):
            print(f"{category:<20} {total:>10.2f}")

        print()

        # Calculate the total amount spent across all categories
        grand_total = sum(totals.values())

        print("-" * TABLE_WIDTH)
        print(f"{'TOTAL':<20} {grand_total:>10.2f}")
        print("-" * TABLE_WIDTH)

    except OSError:
        print("\nError: Unable to read expenses.csv.\n")



def monthly_report():

    """Display all expenses for a selected month and year."""

    TABLE_WIDTH = 75
    monthly_expenses = []

    while True:

        try:
            month = int(input("Enter Month: "))
            if 1 <= month <= 12:
                break
            print("Month must be between 1 and 12.")

        except ValueError:
            print("Please enter valid month.")

    while True:
        try:
            year = int(input("Enter Year: "))
            if 1900 <= year <= 2100:
                break
            print("Year must be between 1900 and 2100.")

        except ValueError:
            print("Please enter valid year.")

    # Convert month number to month name
    month_name = datetime(year, month, 1).strftime("%B")

    try:

        with open(CSV_FILE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            # Skip the header row
            try:
                next(reader)

            except StopIteration:
                print("No data found")
                return
            
            for row in reader:

                # Skip malformed rows (e.g., manually edited CSV)
                if len(row) != 4:
                    continue

                date = datetime.strptime(row[0], "%d-%m-%Y")
                expense_month = date.month
                expense_year = date.year

                # Store expenses that match the selected month and year
                if expense_month == month and expense_year == year:
                    monthly_expenses.append(row)

        if not monthly_expenses:
            print("No expenses in this month.\n")
            return
        
        # Print report headers
        print("=" * TABLE_WIDTH)
        print("MONTHLY REPORT".center(TABLE_WIDTH))
        print("=" * TABLE_WIDTH)
        print(f"Period:         {month_name} {year}")
        print(f"Total Expenses: {len(monthly_expenses)}\n")
        print(f"{'Date':<12} {'Category':<15} {'Description':<35} {'Amount':>10}")
        print("-" * TABLE_WIDTH)

        for row in monthly_expenses:
            print(f"{row[0]:<12} {row[1]:<15} {row[2]:<35} {float(row[3]):>10.2f}")

        print()

        # Calculate the total amount spent for the selected month
        grand_total = sum(float(row[3]) for row in monthly_expenses)

        print("-" * TABLE_WIDTH)

        print(f"{'TOTAL':<64} {grand_total:>11.2f}")

        print("-" * TABLE_WIDTH)


    except OSError:
        print("\nError: Unable to read expenses.csv.\n")


            
            

        