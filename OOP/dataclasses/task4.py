from dataclasses import dataclass, field, asdict
from task1 import Product

@dataclass
class Order:

    order_id: str
    items: list[Product] = field(default_factory=list)

    def to_dict(self):
        return asdict(self)

p1 = Product(1, 20, ['some'])
p2 = Product(2, 25, ['nine'])
p3 = Product(3, 30, [])
order1 = Order('123', [p1, p2, p3])
print(order1.to_dict())