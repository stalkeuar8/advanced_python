
class Compressor:
    def compress(self):
        print("Компресор стискає фреон...")

class SmartFridge:

    def __init__(self):
        self._compressor = Compressor()

    def make_ice(self):
        self._compressor.compress() # Використовує метод батька
        print("Робимо лід...")

fridge = SmartFridge()
fridge.make_ice()