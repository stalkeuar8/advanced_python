from abc import ABC, abstractmethod
import json
import csv

class FileProcessor(ABC):

    @abstractmethod
    def write(self, filename: str, text: str):
        print(f"Written to file\nText: {text}")    
    
    @abstractmethod
    def read(self, filename: str):
        print(f"Reading from file '{filename}'...")


class FormatValidator(ABC):

    @abstractmethod
    def validate_format(self, filename: str):
        pass


class TextFileProcessor(FileProcessor, FormatValidator):

    def write(self, filename, text):
        if self.validate_format(filename):
            # with open(filename, 'w', encoding='utf-8') as file:
            #     file.write(text)
            super().write(filename, text)

    def read(self, filename):
        if self.validate_format(filename):
            super().read(filename)
            # with open(filename, 'r', encoding='utf-8') as file:
            #     info = file.read()
            print("File read successfully.")

    def validate_format(self, filename):
        format = filename.split('.')[-1]
        if not format == 'txt':
            raise TypeError(f"Invalid file type, must be '.txt', got '.{format}' instead.")
        return True
    


class JsonFileProcessor(FileProcessor, FormatValidator):

    def write(self, filename, text):
        if self.validate_format(filename):
            # with open(filename, 'w', encoding='utf-8') as file:
            #     json.dumps(text)
            super().write(filename, text)

    def read(self, filename):
        if self.validate_format(filename):
            super().read(filename)
            # with open(filename, 'r', encoding='utf-8') as file:
            #     info = json.load(file)
            print("File read successfully.")

    def validate_format(self, filename):
        format = filename.split('.')[-1]
        if not format == 'json':
            raise TypeError(f"Invalid file type, must be '.json', got '.{format}' instead.")
        return True
    

class CsvFileProcessor(FileProcessor, FormatValidator):

    def write(self, filename, text):
        if self.validate_format(filename):
            # with open(filename, 'w', encoding='utf-8') as file:
            # logic for CSV writing 
            super().write(filename, text)

    def read(self, filename):
        if self.validate_format(filename):
            super().read(filename)
            # with open(filename, 'r', encoding='utf-8') as file:
            #     logic for CSV reading
            print("File read successfully.")

    def validate_format(self, filename):
        format = filename.split('.')[-1]
        if not format == 'csv':
            raise TypeError(f"Invalid file type, must be '.csv', got '.{format}' instead.")
        return True
    
