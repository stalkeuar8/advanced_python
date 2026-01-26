class Animal:
    __speices = 'Unknown'
    def __init__(self, speices):
        self.__speices = speices

    @property
    def get_species(self):
        return self.__speices
    
    def speak(self):
        print("Hello!")

    def eat(self, smth):
        print(f"Eating {smth}")
    
    def sleep(self):
        print(f"i am sleeping")


class Dog(Animal):
    
    def __init__(self):
        super().__init__(Dog.__name__)

d = Dog()
print(d.get_species)