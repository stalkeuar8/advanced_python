

class Validator:

    def __set_name__(self, obj, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        
        return getattr(obj, self.private_name, None)
    
    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)
        # print(f"Obj {self.private_name} set, value: {value}")


    def validate(self, value):
        pass

class PositiveInt(Validator):

    def __init__(self, min_value=None):
        if min_value:
            self.min_value = min_value
        else:
            self.min_value = None
        

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f"Value '{self.private_name}' must be type 'int', got '{type(value)}' instead.")
        if self.min_value is not None:
            if value < self.min_value:
                raise ValueError(f"Value '{self.private_name}' must be bigger than '{self.min_value}', got '{value}' instead.")
        else:
            if value < 0:
                raise ValueError(f"Value '{self.private_name}' must be bigger than 0, got '{value}' instead.")
            

class NonEmptyString(Validator):
        

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f"Value '{self.private_name}' must be type 'str', got '{type(value)}' instead.")
        if not len(value):
            raise ValueError(f"Value '{self.private_name}' can't be empty.")
