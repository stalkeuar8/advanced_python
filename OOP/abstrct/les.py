from abc import ABC, abstractmethod

class Dog(ABC):

    @abstractmethod
    def work(self):
        pass

    def bark(self):
        print("GAAAAV")

class HuntingDog(Dog): 

    def work(self):
        super().work()
        print("Hunting")

class ShepheredDog(Dog):

     def work(self):
        super().work()
        print("Working")
