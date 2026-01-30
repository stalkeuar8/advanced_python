from type_validators import PositiveInt, NonEmptyString
from json_logic import update_json, read_json
from config import PRODUCTS_INFO_FILE_NAME


class Product:

    _total_products = 0

    @classmethod
    def get_prod_id(cls):
        return Product._total_products

    name = NonEmptyString()
    weight = PositiveInt()
    qty = PositiveInt()

    def __init__(self, name, weight, qty):
        Product._total_products += 1
        self.product_id = Product.get_prod_id()
        self.name = name
        self.weight = weight
        self.qty = qty
        Product._register_product(self.product_id, self.name, self.weight, self.qty)


    @classmethod
    def _init_from_string(cls, string: str):
        name, weight, qty = string.split('-')
        return cls(name, int(weight), int(qty))
    
    @classmethod
    def add_products(cls, *products):
        for product in products:
            Product._init_from_string(product)


    @classmethod
    def all_products(cls):
        products: dict = read_json(PRODUCTS_INFO_FILE_NAME)
        for k, v in products.items():
            yield [k, v['name'], v['weight'], v['qty']]


    @classmethod
    def generate_products_menu(cls):
        products: dict = read_json(PRODUCTS_INFO_FILE_NAME)
        for k, v in products.items():
            yield f"[{k}] {v['name']} (Weight: {v['weight']} kg) - {v['qty']} available now."

    @classmethod
    def _register_product(cls, prod_id: int, name: str, weight: int, qty: int):
        products_info = read_json(PRODUCTS_INFO_FILE_NAME)
        if not name in products_info:
            products_info[prod_id] = {'name': name, 'weight': weight, 'qty': qty}
        update_json(PRODUCTS_INFO_FILE_NAME, products_info)


    @classmethod
    def _clear_products(cls):
        update_json(PRODUCTS_INFO_FILE_NAME, {})
        


    def __str__(self):
        products: dict = read_json(PRODUCTS_INFO_FILE_NAME)
        for k, v in products.items():
            yield f"[{k}] Product: {v['name']}, weight: {v['weight']} kg, qty available: {v['qty']}" 


# try:
#     prods_list = ['macbook pro m5-2-3', 'airpods 3-1-10', 'ecoflow 2kw-15-2']
#     Product.add_products(*prods_list)
#     print("\n")
#     for product in Product.generate_products_menu():
#         print(product)
    


# except Exception as e:
#     print(e)