def main():
    while True:
        print("====== EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category Summary")
        print("4. Monthly Report")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            print("Adding Expense...\n")
            
        elif choice == "2":
            print("Viewing Expenses...\n")

        elif choice == "3":
            print("Viewing Category Summary...\n")
            
        elif choice == "4":
            print("Generating Monthly Report...\n")
            
        elif choice == "5":
            print("EXITING...")
            break
        
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":

    try:
        main()
    
    except(KeyboardInterrupt):
        
        print("\nExiting...")




