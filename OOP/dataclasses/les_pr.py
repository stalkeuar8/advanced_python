from dataclasses import dataclass, asdict


@dataclass
class User:
    name: str
    age: int


class UserHandler:

    def __init__(self, name, age):
        self.user = User(name, age)

    def get_dataclass(self):
        return asdict(self.user)
    
user = UserHandler('bob', 15)
print(user.get_dataclass())

