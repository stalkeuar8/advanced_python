from abc import ABC, abstractmethod

class SetVolume(ABC):

    @abstractmethod
    def set_volume(self, level): pass

class SetTemperature(ABC):

    @abstractmethod
    def set_temperature(self, temp): pass


class SmartDevice(ABC):
    @abstractmethod
    def turn_on(self): pass
    

class SmartTV(SmartDevice, SetVolume):


    def turn_on(self): 
        print("TV is On")

    def set_volume(self, level): 
        print(f"TV Volume: {level}")


class SmartLamp(SmartDevice, SetTemperature):

    def turn_on(self): 
        print("Lamp is On")

    def set_temperature(self, temp): 
        print(f"Color temperature: {temp}")