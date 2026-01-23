
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return f"Rectangle width is: {self._width} sm."
    

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError("Width must be greater than 0!")

    @property
    def height(self):
        return f"Rectangle height is: {self._height} sm."
    

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise ValueError("Height must be greater than 0!")
        
    
    @property
    def perimeter(self):
        return f"Perimeter: {2 * (self._height + self._width)} sm"
    
    @property
    def area(self):
        return f"Area: {self._height * self._width} sm2"

    @property
    def aspect_ratio(self):
        if self._height > self._width:
            return f"Height to width: {round(self._height/self._width, 2)}"
        elif self._height < self._width:
            return f"Width to height: {round(self._width/self._height, 2)}"
        
    
    def resize(self, scale):
        if scale <= 0:
            raise ValueError("Scale must be positive.")
        self._height = round(self._height*scale)
        self._width = round(self._width*scale)
        return f"New width: {self._width}, new height: {self._height}"
    
    def __str__(self):
        return f"\n----\nWidth: {self._width}\nHeight: {self._height}\n----\n"
    
try:

    square = Rectangle(14, 10)
    print(square.width)
    print(square.height)
    print(square.area)
    print(square.aspect_ratio)
    print(square.resize(2))
    print(square.resize(0.25))

except Exception as e:
    print(e)
