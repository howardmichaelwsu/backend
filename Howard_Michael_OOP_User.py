class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.money = 0
    def make_deposit(self, deposit):
        self.money += deposit 
        return self
    def make_withdrawal(self, withdrawal):
        self.money -= withdrawal
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, User Balance: ${self.money}")

michael = User("Michael", "michael@aol.com")
courtney = User("Courtney", "courtney@aol.com")
kai = User("Kai", "kai@aol.com") 

michael.make_deposit(100).make_deposit(100).make_deposit(300).make_withdrawal(150).display_user_balance


courtney.make_deposit(150)
courtney.make_deposit(150)
courtney.make_withdrawal(100)
courtney.make_withdrawal(100)
courtney.display_user_balance()

kai.make_deposit(500)
kai.make_withdrawal(100)
kai.make_withdrawal(100)
kai.make_withdrawal(100)
kai.display_user_balance()