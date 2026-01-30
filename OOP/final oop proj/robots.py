from abc import ABC, abstractmethod
from type_validators import TypeValidator

class Robot(ABC):

    max_load = TypeValidator(int)
    name = TypeValidator(str)


    def __init__(self, name: str, max_load: int):
        pass

    @abstractmethod
    def perform_task(self):
        pass

