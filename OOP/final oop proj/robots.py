from abc import ABC, abstractmethod
from type_validators import PositiveInt, NonEmptyString
from json_logic import update_json, read_json
from config import ROBOTS_INFO_FILE_NAME

class Robot(ABC):

    def __init__(self, name: str, max_load: int):
        self.name = name
        self.max_load = max_load
        self._current_order = None
        self._registrate_robot()
        
    @property
    def is_available(self):
        return self._current_order is None
    
    def assign_order(self, order: dict):
        if self._current_order is not None:
            raise ValueError("Current robot is not available.")
        
        print(f"Robot {self._name} assigned order!")
        self._current_order = order
        self._perform_task(order)

    def _finish_order(self):
        self._current_order = None
        print(f"Robot '{self._name}' finished performing order!")


    @abstractmethod
    def _perform_task(self, order: dict):
        print(f" is performing order {list(order.keys())}")
        self._finish_order()


    def _registrate_robot(self):
        robots_info =  read_json(ROBOTS_INFO_FILE_NAME)
        robots_info[self.name] = self.max_load
        update_json(ROBOTS_INFO_FILE_NAME, robots_info)


class LightWeightRobot(Robot):

    name = NonEmptyString()


    def __init__(self, name):
        max_load = 100
        super().__init__(name, max_load)


    def _perform_task(self, order):
        print(f"Light Weight Robot '{self._name}'", end='')
        super()._perform_task(order)



class MediumWeightRobot(Robot):

    name = NonEmptyString()

    def __init__(self, name):
        max_load = 1000
        super().__init__(name, max_load)


    def _perform_task(self, order):
        print(f"Medium Weight Robot '{self._name}'", end='')
        super()._perform_task(order)


class HeavyWeightRobot(Robot):

    name = NonEmptyString()

    def __init__(self, name):
        max_load = 5000
        super().__init__(name, max_load)


    def _perform_task(self, order: dict):
        print(f"Heavy Weight Robot '{self._name}'", end='')
        super()._perform_task(order)


# lwr1 = LightWeightRobot('lwr1')
# mwr1 = MediumWeightRobot('mwr1')
# hwr1 = HeavyWeightRobot('hwr1')

# orders = read_json('test.json')

# robots = [lwr1, mwr1, hwr1]

# for robot in robots:
#     robot.assign_order(orders)

