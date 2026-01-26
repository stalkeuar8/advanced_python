from abc import abstractmethod, ABC

class DiscountStrategy(ABC):

    @abstractmethod
    def apply_total_sum(self, raw_total):
        return raw_total


class NoDiscount(DiscountStrategy):

    def __init__(self):
        self.disc_perc = 0
    

    def apply_total_sum(self, raw_total):
        return super().apply_total_sum(raw_total)


class PercentageDiscount(DiscountStrategy):

    def __init__(self, percent: int):
        if not isinstance(percent, int):
            raise TypeError('Percent name must be int')
        if not 0 <= percent <= 100:
            raise ValueError("Percent must be between 0 and 100")
        self.disc_perc = percent / 100


    def apply_total_sum(self, raw_total):
        total = int(raw_total - raw_total*self.disc_perc)
        return super().apply_total_sum(total)
    
        
class ThresholdDiscount(DiscountStrategy):

    def __init__(self, disc_amount, disc_minimum):
        self.disc_amount = disc_amount
        self.disc_minimum = disc_minimum
    
    def apply_total_sum(self, raw_total):
        if raw_total < self.disc_minimum:
            return super().apply_total_sum(raw_total)
        total = raw_total - self.disc_amount
        return super().apply_total_sum(total)
        


class Cart:

    def __init__(self):
        self.items = {}
        self.discount_strategy = None

    def strategy_setter(self, strategy: DiscountStrategy):
        self.discount_strategy = strategy
        


    def add_to_cart(self, item, price):
        if not isinstance(item, str):
            raise TypeError('Item name must be str')
        if not item:
            raise ValueError("Item cant be empty")
        if not isinstance(price, (int, float)):
            raise TypeError('Price name must be int or float')
        if price <= 0:
            raise ValueError("Price must be greater than 0")
        self.items[item] = price
        return True

    def total_sum(self):
        total_sum = sum(list(self.items.values()))
        if not self.discount_strategy:
            self.discount_strategy = NoDiscount()
        return self.discount_strategy.apply_total_sum(total_sum)
    
try:

    cart = Cart()
    cart.add_to_cart("iphone", 65000)
    cart.add_to_cart("macbook", 80000)
    cart.add_to_cart("apple watch", 15000)
    print(cart.items)
    print(cart.total_sum())

except Exception as e:
    print(e)