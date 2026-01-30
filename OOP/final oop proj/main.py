from order import OrderItem
from products import Product
from input_parser import StrParser


# prods_list = ['macbook pro m5-2', 'airpods 3-1', 'ecoflow 2kw-15']

# Product.add_products(*prods_list)

for product in Product.generate_products_menu():
    print(product)

user_choice = input("\nEnter your choice in format ('product id':'qty'): ")
print(StrParser.parse(user_choice))



