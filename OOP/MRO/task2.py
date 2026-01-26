from abc import ABC, abstractmethod

class FileParser(ABC):

    @abstractmethod
    def parse(self, file_path):
        pass

class CsvParser(FileParser):

    def __init__(self):
        pass

    def parse(self, file_path):
        print(f"Parsing csv file: {file_path}")

class JsonParser(FileParser):

    def __init__(self):
        pass

    def parse(self, file_path):
        print(f"Parsing json file: {file_path}")


js = JsonParser()
cs = CsvParser()
js.parse("sdfsdfs")
cs.parse("sdfsdfs")