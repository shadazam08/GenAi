class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def get_balance(self):
        print(f"The Total Balance is : {self.__balance}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposit Amount is : {self.get_balance()}"
        else:
            return f"Deposit Amount must be positive"

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdraw {amount} is : {self.get_balance()}"
        else:
            return f"insufficient fund in the account"


account = BankAccount("Shad", 0)

account.deposit(1500000)

account.withdraw(50000)

account.get_balance()

