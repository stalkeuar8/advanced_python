

class Temperature:

    def __init__(self, temp_cels):
        self._celsius = temp_cels

    @property
    def kelvin(self):
        return self._celsius + 273
    
    @kelvin.setter
    def kelvin(self, value):
        if value - 273 < -273:
            raise ValueError("Temperature cant be lower that absolute 0")
        self._celsius = value - 273

        
    @property
    def faringheit(self):
        return (self._celsius * 1.8) + 32
    
    @faringheit.setter
    def faringheit(self, value):
        if (value-32) / 1.8 < -273: 
            raise ValueError("Temperature cant be lower that absolute 0")
        self._celsius = (value-32) / 1.8 


    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273:
            raise ValueError("Temperature cant be lower that absolute 0")
        self._celsius = value


term = Temperature(25)
print(term.kelvin)
print(term.faringheit)
print(term.celsius)

term.celsius = 50
print(term.celsius)
term.kelvin = 500
print(term.celsius)




