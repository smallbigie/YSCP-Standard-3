# Global dictionary to store transactions (description, amount, type)
transactions = {}

# Function to add income
def add_income():
    description = input("Enter the income description: ")
    try:
        amount = float(input("Enter the income amount: "))
        if amount > 0:
            transactions[description] = (amount, 'income')
            print(f"Income of {amount} added: {description}")
        else:
            print("Income amount must be greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")

# Function to add an expense
def add_expense():
    description = input("Enter the expense description: ")
    try:
        amount = float(input("Enter the expense amount: "))
        if amount > 0:
            transactions[description] = (amount, 'expense')
            print(f"Expense of {amount} added: {description}")
        else:
            print("Expense amount must be greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")

# Function to view current balance
def view_balance():
    balance = 0
    for transaction in transactions.values():
        amount, trans_type = transaction
        if trans_type == 'income':
            balance += amount
        elif trans_type == 'expense':
            balance -= amount
    print(f"Current balance: {balance:.2f}")

# Function to view all transactions
def view_all_transactions():
    if transactions:
        print("\n--- All Transactions ---")
        for description, (amount, trans_type) in transactions.items():
            print(f"{description}: {amount:.2f} ({trans_type.capitalize()})")
    else:
        print("No transactions available.")

# Function to remove a transaction
def remove_transaction():
    description = input("Enter the description of the transaction to remove: ")
    if description in transactions:
        del transactions[description]
        print(f"Transaction '{description}' removed.")
    else:
        print(f"Transaction with description '{description}' not found.")

# Main function to run the menu-driven system
def main():
    while True:
        print("\n--- Budget Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Current Balance")
        print("4. View All Transactions")
        print("5. Remove a Transaction")
        print("6. Quit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_income()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            view_balance()
        elif choice == '4':
            view_all_transactions()
        elif choice == '5':
            remove_transaction()
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()
