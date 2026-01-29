from abc import ABC, abstractmethod


class Operation(ABC):

    @abstractmethod
    def execute(self, a, b):
        pass

    @abstractmethod
    def symbol(self):
        pass


class Add(Operation):

    def execute(self, a, b):
        return a + b
    
    def symbol(self):
        return '+'
    

class Mult(Operation):

    def execute(self, a, b):
        return a * b
    
    def symbol(self):
        return '*'
    

class Divide(Operation):

    def execute(self, a, b):
        return a / b
    
    def symbol(self):
        return '/'
    

class Subtract(Operation):

    def execute(self, a, b):
        return a - b
    
    def symbol(self):
        return '-'
    

class Calculator:

    def __init__(self, operations: list[Operation]):
        self.operations = {op.symbol(): op for op in operations}

    
    def calculate(self, a, b, operator):
        if operator not in self.operations:
            raise ValueError("Unknown operator.")
        
        operation = self.operations[operator]
        result = operation.execute(a, b)
        return result
    

calc = Calculator([Add(), Divide(), Subtract(), Mult()])

print(calc.calculate(5, 10, '+'))
print(calc.calculate(5, 10, '*'))
print(calc.calculate(10, 2, '/'))
