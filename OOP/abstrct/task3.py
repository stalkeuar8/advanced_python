from abc import ABC, abstractmethod

class Storage(ABC):

    @abstractmethod
    def save(self, text):
        pass

    @classmethod
    def get(cls, type):
        if type == 'cloud':
            return CloudStorage()
        elif type == 'local':
            return LocalStorage()
        else:
            raise ValueError("Unknown type.")


class CloudStorage(Storage):

    def __init__(self):
        pass

    def save(self, text):
        self.connect_to_cloud()
        print("Text saved to cloud.")

    def connect_to_cloud(self):
        print("Connected to cloud storage.")
    
class LocalStorage(Storage):

    def __init__(self):
        pass

    def save(self, text):
        with open("file.txt", 'a') as file:
            file.write(text)
    