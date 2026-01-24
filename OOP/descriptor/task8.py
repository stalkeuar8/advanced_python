class Name:

    def __get__(self, obj, objtype=None):
        if obj:
            return obj._name.capitalize()
    
    def __set__(self, obj, name):
        if len(name) > 3:
            obj._name = name.lower()
        else:
            raise ValueError("Too short name.")

class Age:

    def __get__(self, obj, objtype=None):
        if obj:
            return obj._age

    was_set = False

    def __set__(self, obj, age_value: int):
        if not Age.was_set:
            if age_value > 30:
                obj._age = age_value
            else:
                raise ValueError("Age error")
        else: raise AttributeError("Cant change Age.")

class Human:

    name = Name()
    age = Age()

    def __init__(self, name, age):
        self.age = age
        self.name = name



try:

    human = Human('bobik', 35)
    print(human.age)
    print(human.name)

except Exception as e:
    print(e)