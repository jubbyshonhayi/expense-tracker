import schedule
import time
from datetime import datetime

from report import monthly_report

def generate_monthly_report():
    """Generate a report for the current month."""

    today = datetime.now()

    monthly_report(today.month, today.year)

schedule.every(1).minutes.do(generate_monthly_report)

print("Automation started...")

while True:
    schedule.run_pending()
    time.sleep(1)