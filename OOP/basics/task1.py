# encapsulation and property
class BankAccount:

    def __init__(self, balance):
        self.balance = balance


    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, balance):
        if balance <= 0:
            raise ValueError("Balance cant be smaller than 0")
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("You cant deposit negative amount or 0")

    def withdraw(self, amount):
        if self._balance - amount >= 0:
            self._balance -= amount
        else:
            raise ValueError("Not enough money to withdraw this amount.")

my_ac = BankAccount(100)
print(my_ac.balance)
my_ac.deposit(1000)
print(my_ac.balance)
my_ac.deposit(0)

