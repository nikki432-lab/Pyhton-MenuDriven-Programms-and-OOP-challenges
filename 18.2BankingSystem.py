class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance}")

    def deposit_money(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully!")
        else:
            print("Invalid deposit amount.")

    def withdraw_money(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully!")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

def main():
    account = BankAccount()

    while True:
        print("\nBanking System Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            account.check_balance()
        elif choice == '2':
            amount = float(input("Enter amount to deposit: ₹"))
            account.deposit_money(amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: ₹"))
            account.withdraw_money(amount)
        elif choice == '4':
            print("Thank you for using our banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
