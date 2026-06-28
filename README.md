Automated Expense Tracker

A Python-based command-line application for tracking personal expenses using CSV file storage. The project demonstrates file handling, data aggregation, automation, modular programming, and data visualization.

⸻

Features

* Add new expenses
* View all recorded expenses
* View category-wise spending summary
* Generate monthly expense reports
* View monthly spending trends in a formatted table
* Visualize monthly spending using line charts (Matplotlib)
* Automatically generate monthly reports using scheduling
* Handles invalid input and malformed CSV records gracefully

⸻

Technologies Used

* Python 3
* CSV
* Datetime
* Matplotlib
* Schedule

⸻

Project Structure

expense-tracker/
│
├── main.py            # Application entry point and menus
├── expenses.py        # Add expenses
├── report.py          # Expense reports and summaries
├── trends.py          # Monthly analytics and insights
├── charts.py          # Data visualization using Matplotlib
├── automation.py      # Scheduled monthly report generation
├── utils.py           # Shared helper functions and constants
├── expenses.csv       # Expense database
└── README.md

⸻

Installation

Clone the repository:

git clone <repository-url>
cd expense-tracker

Install the required packages:

pip install matplotlib schedule

⸻

Running the Application

Start the application with:

python main.py

⸻

Application Menu

====== EXPENSE TRACKER ======
1. Add Expense
2. View Expenses
3. Category Summary
4. Monthly Report
5. Monthly Trends
6. Exit

The Monthly Trends menu provides:

* View monthly trends in a table
* View monthly spending as a line chart

⸻

Sample Monthly Trends Output

============================================================
                     MONTHLY TRENDS
============================================================
Month                   Expenses              Amount
------------------------------------------------------------
June 2026                      8             1240.00
July 2026                     10             1585.50
------------------------------------------------------------
TOTAL                         18             2825.50
------------------------------------------------------------
INSIGHTS
------------------------------------------------------------
Highest Spending Month : July 2026
Average Per Month      : 1412.75
Months Recorded        : 2
============================================================

⸻

Learning Objectives

This project demonstrates practical experience with:

* File handling using CSV
* Functions and modular programming
* Error handling
* Dictionaries and data aggregation
* Date and time processing
* Data visualization with Matplotlib
* Basic automation using scheduled tasks
* Software refactoring and separation of concerns

⸻

Future Improvements

* Overspending alerts
* Category spending charts
* Export reports to PDF
* Excel file support
* Budget tracking
* Search and filter expenses
* Graphical User Interface (GUI)
* Database integration (SQLite/PostgreSQL)

⸻

Author

Jubilant Shonhayi

Built as part of a Python software development learning journey focused on writing clean, modular, and maintainable code.