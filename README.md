# Automated Expense Tracker

A command-line expense tracking application built with Python. The project allows users to record expenses, generate reports, visualize spending trends, and automate monthly report generation.

---

## Features

### Expense Management

- Add new expenses
- Store expenses in a CSV file
- Input validation
- Automatic CSV creation

### Reports

- View all recorded expenses
- Category summary
- Monthly reports
- Export monthly reports as formatted text files

### Analytics

- Monthly spending trends
- Total monthly expenses
- Average monthly spending
- Highest spending month
- Number of recorded months

### Charts

- Monthly spending visualization using Matplotlib

### Automation

- Automatic monthly report generation using the `schedule` library.

---

## Project Structure

```text
ExpenseTracker/
│
├── main.py
├── expenses.py
├── report.py
├── trends.py
├── charts.py
├── automation.py
├── utils.py
├── expenses.csv
├── README.md
└── reports/
```

---

## Technologies Used

- Python 3
- CSV
- datetime
- os
- Matplotlib
- schedule

---

## Running the Project

Install the required packages:

```bash
pip install matplotlib schedule
```

Run the application:

```bash
python main.py
```

---

## Concepts Practiced

- File handling
- CSV processing
- Exception handling
- Data aggregation
- Modular programming
- Automation
- Data visualization
- Git and GitHub

---

## Future Improvements

- Overspending alerts
- Budget tracking
- Yearly analytics
- Category charts
- Search and filter
- Expense editing and deletion
- PDF/Excel report export
- Database integration

---

## Author

Jubilant Shonhayi