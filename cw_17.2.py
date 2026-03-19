class BankAccount:
    account_holder = ""
    balance = 0

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposit:", amount)

    def withdrawal(self, amount):
        self.balance = self.balance - amount
        print("Withdrawal:", amount)

    def display_balance(self):
        print("Current Balance:", self.balance)

acc_holder = BankAccount("John", 0)

print("Account Holder:", acc_holder.account_holder)

acc_holder.deposit(500)

acc_holder.withdrawal(200)

acc_holder.display_balance()