from abc import ABC, abstractmethod

class DiscountTyping(ABC):

    @abstractmethod
    def calculate(self, price):
        pass

class ReqularDiscount(DiscountTyping):

    def calculate(self, price):
        return price
    
class PremiumDiscount(DiscountTyping):

    def calculate(self, price):
        return int(price * 0.8)
    
class VipDiscount(DiscountTyping):

    def calculate(self, price):
        return int(price * 0.5)
    

class DiscountCalculator:

    def calculate_discount(self, discount_type: DiscountTyping, price):
        return discount_type.calculate(discount_type, price=price)

print(DiscountCalculator().calculate_discount(VipDiscount, 1000))
