accounts = {}


#Method to create account
def createAccount(account_number):
    if account_number not in accounts:
        account_info = {}
        account_info['name'] = input("Enter account holder's name: ")

        while True:
            account_type = input("Enter account type (savings/current): ").lower()
            if account_type in ["savings", "current"]: #different type of accounts
                account_info['type'] = account_type
                break
            else:
                print("Invalid account type. Please enter 'savings' or 'current'.")

        while True:
            try:
                initial_balance = float(input("Enter the initial balance: "))
                if initial_balance >= 0:
                    account_info['balance'] = initial_balance
                    account_info['transactions'] = []  # Initialize an empty list for transactions
                    accounts[account_number] = account_info
                    print(f"Account number {account_number} has been created for {account_info['name']} with an initial balance of {initial_balance}")
                    break
                else:
                    print("Initial balance must be a non-negative number.")
            except ValueError:
                print("Invalid input. Please enter a valid number for the initial balance.")
    else:
        print("Account already exists.")



#Method to deposit money
def deposit(account_number):
    if account_number in accounts:
        while True:
            try:
                amount = float(input("How much money do you want to deposit: "))
                if amount >= 0:
                    accounts[account_number]['balance'] += amount
                    accounts[account_number]['transactions'].append(f"Deposited ${amount}")
                    print(f"${amount} has been deposited to account number {account_number}. Total balance is: ${accounts[account_number]['balance']}")
                    break
                else:
                    print("Deposit amount must be a non-negative number.")
            except ValueError:
                print("Invalid input. Please enter a valid number for the deposit amount.")
    else:
        print("Account doesn't exist.")



#Method to withdraw money
def withdraw(account_number):
    if account_number in accounts:
        while True:
            try:
                amount = float(input("Enter the amount you want to withdraw: "))
                if amount >= 0:
                    if amount <= accounts[account_number]['balance']:
                        if accounts[account_number]['type'] == "savings" and amount > accounts[account_number]['balance'] - 500:
                            print("Withdrawal not allowed. Minimum balance of $500 required for savings account.")
                        else:
                            accounts[account_number]['balance'] -= amount
                            accounts[account_number]['transactions'].append(f"Withdrew ${amount}")
                            print(f"${amount} has been withdrawn from account number {account_number}. Remaining balance is ${accounts[account_number]['balance']}")
                        break
                    else:
                        print("Insufficient funds")
                else:
                    print("Withdrawal amount must be a non-negative number.")
            except ValueError:
                print("Invalid input. Please enter a valid number for the withdrawal amount.")
    else:
        print("Account doesn't exist.")



#Method to check balance
def checkBalance(account_number):
    if account_number in accounts:
        print(f"Account number {account_number} (owned by {accounts[account_number]['name']}) has a balance of ${accounts[account_number]['balance']}")
    else:
        print("Account doesn't exist.")


#Method to check transaction history
def viewTransactions(account_number):
    if account_number in accounts:
        print(f"Transaction history for account number {account_number}:")
        for transaction in accounts[account_number]['transactions']:
            print(transaction)
    else:
        print("Account doesn't exist.")


#Initializing the menu
while True:
    print("\nBank Account Simulation Menu:")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. View Transactions")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == "1":
        account_number = input("Enter a new account number: ")
        createAccount(account_number)
    elif choice == "2":
        account_number = input("Enter your account number: ")
        deposit(account_number)
    elif choice == "3":
        account_number = input("Enter your account number: ")
        withdraw(account_number)
    elif choice == "4":
        account_number = input("Enter your account number: ")
        checkBalance(account_number)
    elif choice == "5":
        account_number = input("Enter your account number: ")
        viewTransactions(account_number)
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4/5/6).")
