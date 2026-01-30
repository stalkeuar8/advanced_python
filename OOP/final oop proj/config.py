from dotenv import load_dotenv
import os 

load_dotenv()
JSON_FILE_NAME = os.getenv("JSON_FILE_NAME")

if not JSON_FILE_NAME:
    raise ValueError("Filename does not exists. 'config'")