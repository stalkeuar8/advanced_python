
class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.discount = 0

    
    @property
    def price(self):
        return f"Price: {self._price} dol."
    

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Price must be bigger or equal to 0.")

    @property
    def quantity(self):
        return f"Quantity: {self._quantity}."
    
    @quantity.setter
    def quantity(self, value):
        if value >= 0 and isinstance(value, int):
            self._quantity = value
        else:
            raise ValueError("Quantity must be bigger or equal to 0 and be an integer.")


    @property
    def discount(self):
        return f"Discount: {self._discount} %."
    
    @discount.setter
    def discount(self, value):
        if 100 >= value >= 0:
            self._discount = value
        else:
            raise ValueError("Discount must be between 0 and 100.")
    

    @property
    def final_price(self):
        return f"Final price: {(self._price * self._quantity) - (self._price * self._quantity * self._discount / 100)} dol."
    

    @property
    def total_value(self):
        return f"Total value: {self._price * self._quantity} dol."
    

    def apply_discount(self, percent):
        self.discount = percent
    

try:
    my_item = Product("Monitor", 1000, 10)
    print(my_item.price)
    print(my_item.quantity)
    print(my_item.discount)
    print(my_item.final_price)
    print(my_item.total_value)
    my_item.apply_discount(50)
    print(my_item.final_price)


except Exception as e:
    print(e)