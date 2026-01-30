from json_logic import read_json
from config import PRODUCTS_INFO_FILE_NAME

class StrParser:

    @staticmethod
    def parse(string):
        splitted_string = string.split(', ')
        pairs = {}
        for item in splitted_string:

            prod_id_str, qty_str = item.split(':')

            try:
                prod_id = int(prod_id_str)
                qty = int(qty_str)

            except Exception as e:
                raise e
            
            if StrParser._validate_positive_nums(prod_id, qty):
                if StrParser._validate_existing(prod_id_str, qty):
                    if not qty:
                        continue
                    else:
                        if prod_id in pairs.keys():
                            pairs[prod_id] += qty
                        else:
                            pairs[prod_id] = qty
            else: raise ValueError("Values must be positive!")
        return pairs
    

    @staticmethod
    def _validate_existing(prod_id: str, qty: int):
        prods_info: dict = read_json(PRODUCTS_INFO_FILE_NAME)
        if prod_id not in prods_info.keys():
            raise ValueError(f"Invalid product ID input. Such product '{prod_id}' does not exists.")
        if prods_info[prod_id]['qty'] < qty:
            raise ValueError(f"Not enough available items for product '{prods_info[prod_id]['name']}', max amount: {prods_info[prod_id]['qty']}")
        return True


    def _validate_positive_nums(num1, num2):
        if num1 < 0 or num2 < 0:
            return False
        return True