class Bankaccount:
    num_savings_accounts = 0
    num_current_accoutns = 0

    def __init__(self, account_holder, account_number, balance = 0):
        self._account_holder = account_holder
        self._account_number  = account_number
        self._balance = balance

    def deposit(self,amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self,amount):
        if amount > 0 and  amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew{amount}. New balance: {self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def get_balance(self):
        return self._balance
    
class Savingsaccount(Bankaccount):
    def __init__(self, account_holder, account_number, balance = 0, interest_rate = 0.04):
        super().__init__(account_holder, account_number, balance)
        self.interest_rate = interest_rate
        Bankaccount.num_savings_accounts += 1
    
    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"interest applied: {interest}. New balance: {self._balance}")

class Currentaccount(Bankaccount):
    def __init__(self, account_holder, account_number, balance = 0, overdraft_limit = 1000):
        super().__init__(account_holder, account_number, balance)
        self._overdraft_limit = overdraft_limit
        Bankaccount.num_current_accoutns += 1
    
    def withdraw(self,amount):
        if amount > 0 and (self._balance-amount >= -self._overdraft_limit):
            self._balance -= amount
            print(f"Withdrew{amount}. New balance: {self._balance}")
        else:
            print("Withdrawal exceeds overdraft limit.")

def banking_system():
    accounts = {}

    while True:
        print("\n Banking system menu: ")
        print("1. Create savings account: ")
        print("2. Create current account: ")
        print("3. Deposit money: ")
        print("4. Withdraw money: ")
        print("5. Check balance: ")
        print("6. Apply interest(savings account): ")
        print("7. Delete Account")
        print("8. Display Account counts")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter account holder name: ")
            acc_no = input("Enter account number: ")
            accounts[acc_no] = Savingsaccount(name, acc_no)
            print("Savings account created successfully.")

        elif choice == '2':
            name = input("Enter account holder name: ")
            acc_no = input("Enter account number: ")
            accounts[acc_no] = Currentaccount(name, acc_no)
            print("Current account created successfully.")

        elif choice in ['3', '4', '5', '6']:
            acc_no = input("Enter account number: ")
            if acc_no in accounts:
                account = accounts[acc_no]
                if choice == '3':
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                elif choice == '4':
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                elif choice == '5':
                    print(f"Account Balance: {account.get_balance()}")
                elif choice == '6' and isinstance(account, Savingsaccount):
                    account.apply_interest()
                else:
                    print("Invalid operation for this account type: ")
            else:
                print("Account not found")
        
        elif choice == '7':
            acc_no = input("Enter account number to delete: ")
            if acc_no in accounts:
                account = accounts.pop(acc_no)
                if isinstance(account, Savingsaccount):
                    Bankaccount.num_savings_accounts -= 1
                elif isinstance(account, Currentaccount):
                    Bankaccount.num_current_accoutns -= 1
                    print("Account deleted successfully")
            else:
                print("Account not found")
        
        elif choice == '8':
            print(f"Total saving accounts: {Bankaccount.num_savings_accounts}")
            print(f"Total current accounts: {Bankaccount.num_current_accoutns}")

        elif choice == '9':
            print("Exiting Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. please try again.")

banking_system()


                


                                   
            