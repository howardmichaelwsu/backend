class BankAccount:
    def __init__(self, interest = 0, balance = 0):
        self.interest = interest
        self.balance = balance
	def deposit(self, amount):
        self.balance += amount
        return self
	def withdraw(self, amount):
		if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        return self
	def display_account_info(self):
        print(f"balance: ${self.balance}")
        return self
	def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.interest
        return self
bob = BankAccount(.01, 100)
steve = BankAccount(.03, 1000)

bob.deposit(100).deposit(100).deposit(300).withdraw(100).yield_interest().display_account_info()
steve.deposit(1000).deposit(1000).withdraw(100).withdraw(150).withdraw(150).withdraw(100).yield_interest().display_account_info()