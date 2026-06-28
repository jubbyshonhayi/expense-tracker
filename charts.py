import matplotlib.pyplot as plt
from trends import get_monthly_stats

def monthly_chart():
    """Display monthly spending as a line chart."""

    monthly_stats = get_monthly_stats()

    if not monthly_stats:
        print("No monthly trends found.")
        return
    
    months = []
    totals = []
    counts = []

    for key in sorted(monthly_stats.keys()):
        data = monthly_stats[key]

        months.append(data["name"])
        totals.append(data["total"])
        counts.append(data["count"])

    
    plt.figure(figsize=(10, 5))

    plt.plot(months, totals, marker="o", linewidth="2")

    for month, total in zip(months, totals):
        plt.text(month, total, f"{total:.2f}", ha="center", va="bottom")

    plt.title("Monthly Expense Trends")
    plt.xlabel("Month")
    plt.ylabel("Amount Spent")
    plt.grid(True)

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


