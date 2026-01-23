from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x_value):
        if isinstance(x_value, int):
            self._x = x_value
        else:
            raise TypeError("X value must be int.")
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, y_value):
        if isinstance(y_value, int):
            self._y = y_value
        else:
            raise TypeError("Y value must be int.")

    
    @property
    def distance_from_origin(self):
        return round(sqrt(self._x**2 + self._y**2), 1)
    
    @property
    def quadrant(self):
        if self._x == 0 and self._y == 0:
            return 0
        elif self._x > 0 and self._y > 0:
            return 1
        elif self._x < 0 and self._y > 0: 
            return 2
        elif self._x < 0 and self._y < 0: 
            return 3
        elif self._x > 0 and self._y < 0: 
            return 4
        elif self._x == 0 and self._y != 0:
            return "axis Y"
        elif self._x != 0 and self._y == 0:
            return "axis X"
    
    def distance_to(self, other_point: Point):
        return round(sqrt(pow(self.x - other_point._x, 2) + pow(self.y - other_point._y, 2)), 1)
        

    def __str__(self):
        return f"Point ({self._x}, {self._y})"
    
    def __repr__(self):
        return f"Point ({self._x}, {self._y})"


try:    
    point_a = Point(0, 0)
    print(point_a.x)
    print(point_a.y)
    print(point_a.distance_from_origin)
    print("\n")
    point_b = Point(10, 10)
    print(point_a.distance_to(point_b))
    print("\n")
    print(point_a.quadrant)
    print(point_a)
    

except Exception as e:
    print(e)
