from abc import abstractmethod, ABC
from math import sqrt

class DescValue:

    def __set_name__(self, obj, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return
        
        return getattr(obj, self.private_name, None)

    def __set__(self, obj, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be int or float.")
        if value <= 0:
            raise ValueError("Value must be positive.")

        setattr(obj, self.private_name, value)

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    

class Circle(Shape):

    radius = DescValue()

    def __init__(self, radius):
        self.radius = radius


    def perimeter(self):
        return round(2 * 3.14 * self._radius, 1)

    def area(self):
        return round((self._radius ** 2) * 3.14, 1)


class Rectangle(Shape):

    width = DescValue()
    height = DescValue()

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height


class Triangle(Shape):

    side = DescValue()

    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return self._side * 3

    def area(self):
        return round(pow(self._side, 2)*pow(3, 1/2) / 4, 1)


def print_shape_info(shape: Shape):
    print(f"Shape area: {shape.area(Shape)}\n\
          Shape perimeter: {shape.perimeter(Shape)}")
    

tr = Triangle(5)
rect = Rectangle(10, 5)
circ = Circle(5)

for shape in tr, rect, circ:
    print(shape.area())
    print(shape.perimeter())
    print("")