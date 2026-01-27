from menu import Coffee, Dessert

try:

    coffee_1 = Coffee("Americano", 50, 300)
    print(coffee_1.show_details())
    coffee_2 = Coffee.from_string("Latte-80-500")
    print(coffee_2.show_details())
    dessert_1 = Dessert("Croissant", 70, True)
    print(dessert_1.show_details())
    dessert_1.secret_ingredient = 50    
except Exception as e:
    print(e)