from abc import abstractmethod, ABC

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):

    def make_sound(self):
        print("WOOOOOFFFF!")

class Cat(Animal):

    def make_sound(self):
        print("MEEEOOOOWWW!")

class Cow(Animal):

    def make_sound(self):
        print("Cow's sound.")

def animal_concert(*args: Animal):
    for animal in args:
        animal.make_sound(Animal)



dog = Dog()
cat = Cat()
cow = Cow()

animal_concert(dog, cat, cow)