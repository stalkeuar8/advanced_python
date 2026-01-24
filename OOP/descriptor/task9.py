

class CleverWallet:
    def __init__(self):
        self.balance = 0

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cant be negative.")
        self._balance = value
        print(f"Balance set to: {self._balance}")


try:

    my_bal = CleverWallet()
    print(my_bal.balance)
    my_bal.balance = 100
    print(my_bal.balance)

except Exception as e:
    print(e)
    