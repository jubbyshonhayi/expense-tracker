from expenses import add_expense, view_expenses, category_summary, monthly_report

def main():
    
    while True:
      
        print("====== EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category Summary")
        print("4. Monthly Report")
        print("5. Exit\n")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_expense()

            
        elif choice == "2":
            view_expenses()

        elif choice == "3":
            category_summary()

        elif choice == "4":
            monthly_report()
            
        elif choice == "5":
            print("EXITING...")
            break
        
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":

    try:
        main()

    
    except KeyboardInterrupt:

        print("\nExiting...")




