#here is the BankAccount class
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Not enough money")

#here is a bank account object
bank_account = BankAccount("Samal", 300)
#here are some deposits and withdrawals
bank_account.deposit(90)
bank_account.withdraw(80)
bank_account.withdraw(100)
#here is the current balance
print(bank_account.balance)
