class PaymentProcessor:

    def __init__(self):
        pass

    @staticmethod
    def validator(amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be int or float.")
        if amount <= 0:
            raise ValueError("Amount must be greater that 0.")
        return True
    

    def process_payment(self, amount):
        if PaymentProcessor.validator(amount):
            return f"Payment {amount} is successful."
            

    
    

class CommissionMixin:

    def process_payment(self, amount):
        new_amount = amount*0.95
        print(f"Comission taken. {new_amount}")
        return super().process_payment(new_amount)

    
class StripePayment(CommissionMixin, PaymentProcessor):

    def __init__(self):
        super().__init__()

    def process_payment(self, amount):
        return super().process_payment(amount)
    
class CryptoPayment(PaymentProcessor):
    
    def __init__(self, wallet_address):
        super().__init__()
        self.wallet_address = wallet_address
    
    def process_payment(self, amount):
        res = super().process_payment(amount) + f"\nPayment wallet address: {self.wallet_address}"
        return res
    
try:
    crypto = CryptoPayment('qweq343rewr23rfset42')
    print(crypto.process_payment(300))
    print(StripePayment().process_payment(200))
except Exception as e:
    print(e)
