import json 
from pathlib import Path
from config import JSON_FILE_NAME


def is_file_exists(filepath):
    if not Path(filepath).exists():
        with open(filepath, 'w') as file:
            json.dump(obj={}, fp=file)

    return True
    

def get_abs_path(filename):
    path = Path(__file__).parent / filename
    return path


def read_json(filename):
    path = get_abs_path(filename)
    if is_file_exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            info_dict = json.load(file)
            
        return info_dict


def update_json(filename, updated_dict):
    path = get_abs_path(filename)
    if is_file_exists(path):
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(updated_dict, file)
            return True
    
    return False
