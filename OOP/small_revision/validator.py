

class ValidatorTypes:

    def __init__(self, needed_type):
        self.needed_type = needed_type

    def __set_name__(self, objtype, name):
        self.name = name
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        
        return getattr(obj, self.private_name, None)


    def __set__(self, obj, value):

        if not isinstance(value, self.needed_type):
            raise TypeError(f"Value '{self.private_name}' must be {self.needed_type}, got '{type(value)}' instead.")
        
        if isinstance(value, str):
            if not len(value):
                raise ValueError(f"Value '{self.private_name}' cant be empty.")
        
        if isinstance(value, int):
            if value <= 0:
                raise ValueError(f"Value '{self.private_name}' must be positive.")
        
        setattr(obj, self.private_name, value)