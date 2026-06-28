import csv
from datetime import datetime
from utils import  CSV_FILE

def read_monthly_data():
    """Read and clean CSV data for monthly analytics."""

    rows = []

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
                if len(row) != 4:
                    continue
                rows.append(row)

    except OSError:
        print("Error: Unable to read CSV file")
        return []

    return rows


def calculate_monthly_stats(rows):
    """Convert raw rows into monthly analytics data."""

    monthly_stats = {}

    for row in rows:

        try:
            date = datetime.strptime(row[0], "%d-%m-%Y")
            amount = float(row[3])
        except ValueError:
            continue

        month_key = date.strftime("%Y-%m")
        month_name = date.strftime("%B %Y")

        if month_key not in monthly_stats:
            monthly_stats[month_key] = {
                "name": month_name,
                "count": 0,
                "total": 0.0
            }

        monthly_stats[month_key]["count"] += 1
        monthly_stats[month_key]["total"] += amount

    return monthly_stats


def display_monthly_dashboard(monthly_stats):
    """Print formatted monthly analytics dashboard."""

    TABLE_WIDTH = 60

    print("=" * TABLE_WIDTH)
    print("MONTHLY TRENDS".center(TABLE_WIDTH))
    print("=" * TABLE_WIDTH)

    print(f"{'Month':<20}{'Expenses':>15}{'Amount':>20}")
    print("-" * TABLE_WIDTH)

    grand_total = 0
    grand_count = 0

    highest_month = None
    highest_amount = 0

    for key in sorted(monthly_stats.keys()):
        data = monthly_stats[key]

        print(f"{data['name']:<20}{data['count']:>15}{data['total']:>20.2f}")

        grand_total += data["total"]
        grand_count += data["count"]

        if data["total"] > highest_amount:
            highest_amount = data["total"]
            highest_month = data["name"]

    months = len(monthly_stats)
    average = grand_total / months if months else 0

    print("-" * TABLE_WIDTH)
    print(f"{'TOTAL':<20}{grand_count:>15}{grand_total:>20.2f}")
    print("-" * TABLE_WIDTH)

    print()
    print("INSIGHTS")
    print("-" * TABLE_WIDTH)
    print(f"Highest Spending Month : {highest_month}")
    print(f"Average / Month         : {average:.2f}")
    print(f"Months Recorded         : {months}")
    print("=" * TABLE_WIDTH)

def monthly_trends():
    """Controller function for monthly analytics dashboard."""

    rows = read_monthly_data()
    if not rows:
        return

    monthly_stats = calculate_monthly_stats(rows)

    if not monthly_stats:
        print("No monthly trends found.")
        return

    display_monthly_dashboard(monthly_stats)