from abc import ABC, abstractmethod


class AmountValidator:

    def __set_name__(self, obj, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
    
        return getattr(obj, self.private_name, None)
    
    def __set__(self, obj, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Value must be int or float, got '{type(value)}' instead.")
        if value <= 0:
            raise ValueError("Value must be positive.")

        setattr(obj, self.private_name, value)


class ComissionMixin(ABC):

    @abstractmethod
    def calculate_comission(self, amount):
        pass


class PaymentMethod(ABC):

    @abstractmethod
    def process_payment(self, amount):
        print("Payment processed, amount: ", amount)


class Paypal(PaymentMethod):

    amount = AmountValidator()

    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        super().process_payment(self._amount)


class CreditCard(PaymentMethod, ComissionMixin):

    amount = AmountValidator()

    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        total_amount = self.calculate_comission(self._amount)
        print("Commission is: ", self._amount-total_amount)
        super().process_payment(total_amount)

    def calculate_comission(self, amount):
        return int(amount * 0.95)


class Crypto(PaymentMethod, ComissionMixin):

    amount = AmountValidator()

    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        total_amount = self.calculate_comission(self._amount)
        print("Commission is: ", self._amount-total_amount)
        super().process_payment(total_amount)

    def calculate_comission(self, amount):
        amount = int(amount * 0.99) - 2
        if amount <= 0:
            raise ValueError("Small amount. Not enough for comission.")
        return amount
    
credit_payment = CreditCard(1000)
crypto_payment = Crypto(10000)
paypal_payment = Paypal(700)

payments = [credit_payment, crypto_payment, paypal_payment]

for payment in payments:
    payment.process_payment()
