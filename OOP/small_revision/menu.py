from abc import ABC, abstractmethod
from validator import ValidatorTypes

class MenuItem(ABC):

    @abstractmethod
    def show_details(self):
        pass

class Coffee(MenuItem):

    coffee_name = ValidatorTypes(str)
    coffee_price = ValidatorTypes(int)
    coffee_volume = ValidatorTypes(int)

    def __init__(self, coffee_name: str, coffee_price: int, coffee_volume: int):
        self.coffee_name = coffee_name
        self.coffee_price = coffee_price
        self.coffee_volume = coffee_volume

    
    def show_details(self):
        return f"Coffee: {self._coffee_name}, price: {self._coffee_price}, volume: {self._coffee_volume}."


    @classmethod
    def from_string(cls, string: str):
        name, price, volume = string.split("-")
        return cls(name, int(price), int(volume))



class Dessert(MenuItem):

    dessert_name = ValidatorTypes(str)
    dessert_price = ValidatorTypes(int)

    def __init__(self, dessert_name: str, dessert_price: int, dessert_sugar: bool):
        self.dessert_name = dessert_name
        self.dessert_price = dessert_price
        self.dessert_sugar = dessert_sugar
        self._secret_ingredient = "Secret Ingredient"

    @property
    def dessert_sugar(self):
        return self._dessert_sugar

    @dessert_sugar.setter
    def dessert_sugar(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("Sugar existing value must be bool.")
        self._dessert_sugar = value

    @property
    def secret_ingredient(self):
        raise PermissionError("It's a secret! You can't see secret ingredient, if you are not admin.")

    @secret_ingredient.setter
    def secret_ingredient(self, value):
        raise PermissionError("You can't set secret ingredient, if you are not admin.")

    def show_details(self):
        return f"Dessert: {self._dessert_name}, price: {self._dessert_price}, sugar existing: {"yes" if self._dessert_sugar else "no"}."


    @classmethod
    def from_string(cls, string: str):
        name, price, sugar = string.split('-')
        return cls(name, int(price), int(sugar))
    


