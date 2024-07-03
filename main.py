# BANKING SYSTEM

class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited amount to account {self.account_number} is:{
                  amount}.New Balance is : {self.balance}")
            return "Done!!!"
        else:
            print("Deposit must be positive!!")
            return "Please do it again"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn amount to account {self.account_number} is:{
                  amount}.Remaining Balance is : {self.balance}")
            return "Done!!!"
        else:
            print("Withdrawn amount is either negative or greater than balance!!")
            return "Withhdraw again!!"

    def check_balance(self):
        return self.balance


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_number, account_holder):
        account = Account(account_number, account_holder)
        self.accounts.append(account)
        print(f"Account {account_number} created for {account_holder}.")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
            else:
                return "Account does not exist!!"

    def deposit_to_account(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
        else:
            return f"There is no account for account number:{account_number}"

    def withdraw_from_account(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print(f"Account {account_number} not found.")

    def check_account_balance(self, account_number):
        account = self.find_account(account_number)
        if account:
            return account.check_balance()
        else:
            print(f"Account {account_number} not found.")
            return None
