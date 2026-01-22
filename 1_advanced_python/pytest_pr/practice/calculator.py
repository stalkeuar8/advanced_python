from typing import Union

class Calculator:

    def add(self, a: Union[int, float], b: Union[int, float]) -> int | float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both a and b must be nums")
        return a + b

    def subtract(self, a: Union[int, float], b: Union[int, float]) -> int | float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both a and b must be nums")
        return a - b

    def multiply(self, a: Union[int, float], b: Union[int, float]) -> int | float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both a and b must be nums")
        return a * b

    def divide(self, a: Union[int, float], b: Union[int, float]) -> int | float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both a and b must be nums")
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

