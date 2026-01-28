from abc import ABC, abstractmethod

class Bird(ABC):

    @abstractmethod
    def eat(self):
        print("I am eating!")
        

class FlyingBird(ABC):

    @abstractmethod
    def fly(self):
        print("I am flying high!")


class GoingBird(ABC):

    @abstractmethod
    def move(self):
        print("I am moving straight")


class Sparrow(Bird, FlyingBird):

    def eat(self):
        super().eat()

    def fly(self):
        FlyingBird.fly(FlyingBird)

class Ostrich(Bird, GoingBird):

    def eat(self):
        super().eat()

    def move(self):
        GoingBird.move(GoingBird)

def make_bird_fly(bird: FlyingBird):
    try:
        bird.fly()
    except Exception as e:
        print(f"Error: {e}")

def make_bird_move(bird: GoingBird):
    try:
        bird.move()
    except Exception as e:
        print(f"Error: {e}")

sparrow = Sparrow()
make_bird_fly(sparrow)

ostrich = Ostrich()
make_bird_move(ostrich)