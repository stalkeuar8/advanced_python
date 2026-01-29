from dataclasses import dataclass, field, asdict

@dataclass
class Product:

    id: int
    price: float
    ingredients: list = field(default_factory=list)


class ProductsHandler:

    def __init__(self, id, price, ingredients):
        self.prod = Product(id, price, ingredients)

    
capp = ProductsHandler(1, 60.0, ['milk', 'coffee', 'sugar'])
print(asdict(capp.prod))
water = ProductsHandler(2, 15.0, [])
print(asdict(water.prod))

