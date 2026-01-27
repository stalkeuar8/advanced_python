from abc import ABC, abstractmethod


class PayLog(ABC):

    @abstractmethod
    def pay(self, amount, pincode):
        if not isinstance(amount, int):
            raise TypeError("Amount must be int.")
        if not isinstance(pincode, int):
            raise TypeError("Pincode must be int.")
        print(f"Logging.. amount: {amount}")


class GooglePayAccount(PayLog):

    def __init__(self, holder_name, pincode):
        self.holder_name = holder_name
        self.pincode = pincode

    @property 
    def pincode(self):
        return self.__pincode
    
    @pincode.setter
    def pincode(self, pincode):
        if not isinstance(pincode, int):
            raise TypeError("Pincode must be int")
        if not 999 < pincode < 10000:
            raise ValueError("Pincode must be positive and has 4 digits")
        print(f"New pincode set: {pincode}")
        self.__pincode = pincode

    
    def pay(self, amount, pincode):
        super().pay(amount, pincode)
        if not pincode == pincode:
            raise ValueError("Incorrect pincode.")
        print(f"[GooglePay] Pay successful. Amount: {amount}")


class ApplePay(PayLog):

    def __init__(self, apple_id, pincode):
        self.apple_id = apple_id
        self.__pincode = pincode

    @property 
    def pincode(self):
        return self.__pincode
    
    @pincode.setter
    def pincode(self, pincode):
        print(f"New pincode set: {pincode}")
        self.__pincode = pincode

    def pay(self, amount, pincode):
        super().pay(amount, pincode)
        if not pincode == pincode:
            raise ValueError("Incorrect pincode.")
        print(f"[ApplePay] Pay successful. Amount: {amount}")
