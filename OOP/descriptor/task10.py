from typing import Union

class Typing:

    def __init__(self, type, min_value=None):
        self.type = type
        self.min_value = min_value

    def __set_name__(self, owner, name):
        self.name = name
        self.private_name = '_' + name

    def __get__(self, instance, owner=None):
        if instance is None:
            return self

        return getattr(instance, self.private_name, None)
    
    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError(f"Wrong type: {self.name}. Needed '{self.type}', got '{type(value)}' instead.")
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"Value '{self.name}' must be bigger than '{self.min_value}', got '{value}' instead.")
        setattr(instance, self.private_name, value)

class Product:

    name = Typing(str)
    price = Typing((int, float), min_value=0)
    quantity = Typing(int, min_value=0)

    def __init__(self, name: str, price: Union[int, float], quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}. Price: {self.price} dolars. Quantity: {self.quantity}."

try:
    my_prod = Product("Iphone 16 Pro", 1199, 15)
    print(my_prod.name)
    print(my_prod.price)
    print(my_prod.quantity)
    print(my_prod)
except Exception as e:
    print(e)