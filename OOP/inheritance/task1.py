from abc import ABC, abstractmethod 
import os
from pathlib import Path

class BaseDataSource(ABC):

    def read_raw_file(self, path: str):
        path_res = self.validate_path(path)
        if path_res:
            content = []
            with open(path_res, 'r', encoding='utf-8') as file:
                for line in file:
                    content.append(line)
            return content

    @abstractmethod
    def load_data(self, path: str) -> list:
        pass


    def validate_path(self, path: str):
        if not isinstance(path, str):
            raise TypeError("File path must be str.")
        abs_path = (Path(__file__).parent / path).absolute()
        if not os.path.exists(abs_path):
            raise FileExistsError("File does not exists")
        return abs_path 
    
class JsonSource(BaseDataSource):

    def __init__(self, path):
        self.path = path


    def load_data(self, path):
        content_list = super().load_data(path=path)
        content_dict = {}
        for idx, line in enumerate(content_list):
            content_dict[idx] = line
        return content_dict


class CsvSource(BaseDataSource):

    def __init__(self, path):
        self.path = path


    def load_data(self, path):
        return super().load_data(path=path)




try:
    path1 = "somedata1.txt"
    path2 = 'somedata2.txt'
    json_obj = JsonSource(path=path1)
    res1 = json_obj.load_data(path=path1)
    print(res1)
    csv_obj = CsvSource(path=path2)
    res2 = csv_obj.load_data(path=path2)
    print(res2)
except Exception as e:
    print(e)


