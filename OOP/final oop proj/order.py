from type_validators import PositiveInt, NonEmptyString
from json_logic import update_json, read_json
from config import ORDERS_INFO_FILE_NAME
from random import randint
from dataclasses import dataclass, field

@dataclass
class OrderItem:

    order_id: int
    items: list = field(default_factory=list)

    @staticmethod
    def get_order_id():
        while True:
            order_id = randint(10000, 999999)
            if not order_id in read_json(ORDERS_INFO_FILE_NAME).keys():
                return order_id
    
    order_id = PositiveInt()


    @classmethod
    def new_order(cls, items: list):
        order_id = OrderItem.get_order_id()
        OrderItem._register_order(order_id, items)
        print(f"Order created, id: {order_id}, items: {items}")
        return cls(order_id, items)

    @classmethod
    def _register_order(cls, order_id, items):
        order_info = read_json(ORDERS_INFO_FILE_NAME)
        order_info[order_id] = {items[0]:items[1]}
        update_json(ORDERS_INFO_FILE_NAME, order_info)



