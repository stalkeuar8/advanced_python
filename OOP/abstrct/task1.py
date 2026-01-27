info = {
    'americano' : {'price' : 199, 'qty': 25},
    'espr' : {'price' : 100, 'qty': 5},
    'latte' : {'price' : 19, 'qty': 2},
}


class Ingredient:

    names = []

    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty
        Ingredient.names.append(self.name)

    @classmethod
    def from_dict(cls, coffee_info_dict: dict):
        if not isinstance(coffee_info_dict, dict):
            raise TypeError(f"Info must be dict, got '{type(coffee_info_dict)}' instead.")
        if not coffee_info_dict:
            raise ValueError("Info cant be empty.")
        return [cls(k, v['price'], v['qty']) for k, v in coffee_info_dict.items()]


    @classmethod
    def from_str(cls, milk_info_string: str):
        if not isinstance(milk_info_string, str):
            raise TypeError(f"Info must be str, got '{type(milk_info_string)}' instead.")
        if not milk_info_string:
            raise ValueError("Info cant be empty.")
        name, price, qty = milk_info_string.split(',')
        return cls(name, int(price), int(qty))












