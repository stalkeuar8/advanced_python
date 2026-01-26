
class LogMixin:

    def log(self, message):
        print(f"[LOG] : {message}")

class ToDictMixin:

    def to_dict(self):
        return(self.__dict__)
    

class Order(LogMixin, ToDictMixin):
    
    def __init__(self, id, price):
        self.id = id
        self.price = price
        self.log(f"Order created. id: {self.id}, price: {self.price}")

order = Order(111, 299)
print(order.to_dict())