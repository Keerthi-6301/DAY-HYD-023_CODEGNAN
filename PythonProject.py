from datetime import datetime
# BANKING TRANSACTION MANAGEMENT SYSTEM

# MEMBER 1 
# CUSTOMER & ACCOUNT MODULE

class Customer:
    def __init__(self, customer_id, name, age, phone, address):
        self.customer_id = customer_id
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address

    def display(self):
        print("\nCustomer ID:", self.customer_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Phone:", self.phone)
        print("Address:", self.address)


class Account:
    MINIMUM_BALANCE = 500

    def __init__(self, account_no, customer_id, account_type, balance):
        self.account_no = account_no
        self.customer_id = customer_id
        self.account_type = account_type
        self.__balance = balance
        self.status = "Active"

    def get_balance(self):
        return self.__balance


class SavingsAccount(Account):
    def __init__(self, account_no, customer_id, balance):
        super().__init__(
            account_no,
            customer_id,
            "Savings",
            balance)


class CurrentAccount(Account):
    def __init__(self, account_no, customer_id, balance):
        super().__init__(
            account_no,
            customer_id,
            "Current",
            balance)


customers = {}
accounts = {}


# 1. CUSTOMER REGISTRATION
def customer_registration():

    customer_id = input("Enter Customer ID: ")

    if customer_id in customers:
        print("Customer already exists!")
        return

    name = input("Enter Name: ")

    try:
        age = int(input("Enter Age: "))

        if age <= 0:
            raise ValueError("Age must be greater than 0")

    except ValueError as e:
        print("Error:", e)
        return

    phone = input("Enter Phone: ")
    address = input("Enter Address: ")

    customers[customer_id] = Customer(
        customer_id,
        name,
        age,
        phone,
        address
    )

    print("Customer registered successfully!")


# 2. ACCOUNT CREATION
def account_creation():

    customer_id = input("Enter Customer ID: ")

    if customer_id not in customers:
        print("Customer not found!")
        return

    account_no = input("Enter Account Number: ")

    if account_no in accounts:
        print("Account already exists!")
        return

    print("\n1. Savings Account")
    print("2. Current Account")

    choice = input("Enter choice: ")

    try:
        balance = float(input("Enter Initial Balance: "))

        if balance < Account.MINIMUM_BALANCE:
            raise ValueError(
                "Minimum balance is Rs.500"
            )

    except ValueError as e:
        print("Error:", e)
        return

    if choice == "1":

        account = SavingsAccount(
            account_no,
            customer_id,
            balance
        )

    elif choice == "2":

        account = CurrentAccount(
            account_no,
            customer_id,
            balance
        )

    else:
        print("Invalid choice!")
        return

    accounts[account_no] = account

    print("Account created successfully!")


# 7. MINIMUM BALANCE VALIDATION
def minimum_balance_validation():

    account_no = input("Enter Account Number: ")

    if account_no not in accounts:
        print("Account not found!")
        return

    account = accounts[account_no]

    balance = account.get_balance()

    print("\nCurrent Balance: Rs.", balance)

    if balance >= Account.MINIMUM_BALANCE:
        print("Minimum balance requirement satisfied.")
    else:
        print("Minimum balance requirement NOT satisfied.")


# MEMBER 2 
# TRANSACTION MODULE

transactions = {}
def add_transaction(account_no, transaction_type, amount):

    transaction = {
        "date": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"),
        "type": transaction_type,
        "amount": amount
    }

    if account_no not in transactions:
        transactions[account_no] = []

    transactions[account_no].append(transaction)

    # Save transaction to file
    with open("transactions.txt", "a") as file:

        file.write(
            account_no + "|" +
            transaction["date"] + "|" +
            transaction_type + "|" +
            str(amount) + "\n")


# 3. DEPOSIT
def deposit():

    account_no = input("Enter Account Number: ")

    if account_no not in accounts:
        print("Account not found!")
        return

    account = accounts[account_no]

    if account.status == "Closed":
        print("Account is closed!")
        return

    try:

        amount = float(input("Enter Deposit Amount: "))

        if amount <= 0:
            raise ValueError("Amount must be greater than 0")

        # Update private balance
        account._Account__balance += amount

        # Record transaction
        add_transaction(
            account_no,
            "Deposit",
            amount )

        print("\nDeposit successful!")
        print("Current Balance: Rs.",account.get_balance())

    except ValueError as e:
        print("Error:", e)


# 4. WITHDRAWAL
def withdrawal():

    account_no = input("Enter Account Number: ")

    if account_no not in accounts:
        print("Account not found!")
        return

    account = accounts[account_no]

    if account.status == "Closed":
        print("Account is closed!")
        return

    try:

        amount = float(input("Enter Withdrawal Amount: "))

        if amount <= 0:
            raise ValueError("Amount must be greater than 0")

        if (account.get_balance() - amount< Account.MINIMUM_BALANCE):
            raise ValueError("Minimum balance of Rs.500 required")

# Update private balance
        account._Account__balance -= amount

# Record transaction
        add_transaction(
            account_no,
            "Withdrawal",
            amount)

        print("\nWithdrawal successful!")
        print("Current Balance: Rs.",account.get_balance())

    except ValueError as e:
        print("Error:", e)


# 5. FUND TRANSFER
def fund_transfer():

    sender_no = input("Enter Sender Account: ")

    receiver_no = input("Enter Receiver Account: ")

    if sender_no not in accounts:
        print("Sender account not found!")
        return

    if receiver_no not in accounts:
        print("Receiver account not found!")
        return

    if sender_no == receiver_no:
        print("Cannot transfer to the same account!")
        return

    sender = accounts[sender_no]
    receiver = accounts[receiver_no]

    if sender.status == "Closed":
        print("Sender account is closed!")
        return

    if receiver.status == "Closed":
        print("Receiver account is closed!")
        return

    try:

        amount = float(input("Enter Transfer Amount: "))

        if amount <= 0:
            raise ValueError("Amount must be greater than 0")

        if (sender.get_balance() - amount< Account.MINIMUM_BALANCE):
            raise ValueError("Minimum balance of Rs.500 required")

        # Transfer money
        sender._Account__balance -= amount
        receiver._Account__balance += amount

        # Record sender transaction
        add_transaction(
            sender_no,
            "Transfer Sent to " + receiver_no,
            amount)

        # Record receiver transaction
        add_transaction(
            receiver_no,
            "Transfer Received from " + sender_no,
            amount)

        print("\nTransfer successful!")

        print("Sender Balance: Rs.",
            sender.get_balance())

        print("Receiver Balance: Rs.",receiver.get_balance())

    except ValueError as e:
        print("Transfer failed:", e)


# 6. BALANCE ENQUIRY
def balance_enquiry():

    account_no = input("Enter Account Number: ")

    if account_no not in accounts:
        print("Account not found!")
        return

    account = accounts[account_no]

    print("\n========== ACCOUNT DETAILS ==========")

    print("Account Number:",account.account_no)

    print("Customer ID:",account.customer_id)

    print("Account Type:",account.account_type)

    print("Balance: Rs.",account.get_balance())

    print("Status:",account.status)


# MEMBER 3 
# RECORDS & CLOSURE MODULE



# 8. TRANSACTION HISTORY
def transaction_history():

    account_no = input("Enter Account Number: ")

    if account_no not in accounts:
        print("Account not found!")
        return

    print("\n========== TRANSACTION HISTORY ==========")

    found = False

    # First check current program transactions
    if account_no in transactions:

        for t in transactions[account_no]:

            found = True

            print("\nDate   :", t["date"])
            print("Type   :", t["type"])
            print("Amount : Rs.", t["amount"])
            print("-----------------------------------")

    # Also read saved transactions
    try:

        with open("transactions.txt", "r") as file:

            for line in file:

                data = line.strip().split("|")

                if len(data) == 4:

                    acc_no = data[0]

                    if acc_no == account_no:

                        # Avoid duplicate display
                        # when current transaction is already shown
                        if not (
                            account_no in transactions
                            and any(
                                t["date"] == data[1]
                                and t["type"] == data[2]
                                and str(t["amount"]) == data[3]
                                for t in transactions[account_no])):

                            found = True

                            print("\nDate   :", data[1])
                            print("Type   :", data[2])
                            print(
                                "Amount : Rs.",
                                data[3])

                            print("-----------------------------------")

    except FileNotFoundError:
        pass

    if not found:
        print("No transactions found.")


# 9. ACCOUNT CLOSURE
def account_closure():

    account_no = input("Enter Account Number: ")

    if account_no not in accounts:
        print("Account not found!")
        return

    account = accounts[account_no]

    if account.status == "Closed":
        print("Account is already closed!")
        return

    if account.get_balance() != 0:

        print("Balance must be zero before closure.")

        print("Current Balance: Rs.",account.get_balance())

        return

    account.status = "Closed"

# Record account closure
    add_transaction(
        account_no,
        "Account Closed",0)

    print("Account closed successfully!")


# 10. SIMPLE ACCOUNT RECORD STORAGE
def save_account_record(account):

    with open("accounts.txt", "a") as file:

        file.write(
            account.account_no + "|" +
            account.customer_id + "|" +
            account.account_type + "|" +
            str(account.get_balance()) + "|" +
            account.status + "\n")

    print("Account record saved successfully!")


def save_all_accounts():

    if not accounts:
        print("No accounts available!")
        return

    # Write all current accounts
    with open("accounts.txt", "w") as file:

        for account in accounts.values():

            file.write(
                account.account_no + "|" +
                account.customer_id + "|" +
                account.account_type + "|" +
                str(account.get_balance()) + "|" +
                account.status + "\n")

    print("All account records saved to accounts.txt")


# MAIN MENU 

def main():

    while True:

        print("\n")
       
        print(" BANKING TRANSACTION MANAGEMENT SYSTEM")
        

        print("1. Customer Registration")
        print("2. Account Creation")
        print("3. Deposit")
        print("4. Withdrawal")
        print("5. Fund Transfer")
        print("6. Balance Enquiry")
        print("7. Minimum Balance Validation")
        print("8. Transaction History")
        print("9. Account Closure")
        print("10. Simple Account Record Storage")
        print("11. Exit")

        

        choice = input("Enter your choice: ")

        if choice == "1":

            customer_registration()

        elif choice == "2":

            account_creation()

        elif choice == "3":

            deposit()

        elif choice == "4":

            withdrawal()

        elif choice == "5":

            fund_transfer()

        elif choice == "6":

            balance_enquiry()

        elif choice == "7":

            minimum_balance_validation()

        elif choice == "8":

            transaction_history()

        elif choice == "9":

            account_closure()

        elif choice == "10":

            save_all_accounts()

        elif choice == "11":

           

            print("Your trust is our priority. Thank you for using our service")

            break

        else:

            print("Invalid choice. Please try again.")


#START PROGRAM 

if __name__ == "__main__":
    main()
