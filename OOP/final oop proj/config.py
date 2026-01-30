from dotenv import load_dotenv
import os 

load_dotenv()
ORDERS_INFO_FILE_NAME = os.getenv("ORDERS_INFO_FILE_NAME")
ROBOTS_INFO_FILE_NAME = os.getenv("ROBOTS_INFO_FILE_NAME")
PRODUCTS_INFO_FILE_NAME = os.getenv("PRODUCTS_INFO_FILE_NAME")

if not ORDERS_INFO_FILE_NAME:
    raise ValueError("Filename 'ORDERS_FILE_NAME' does not exists. 'config'")

if not ROBOTS_INFO_FILE_NAME:
    raise ValueError("Filename 'ROBOTS_INFO_FILE_NAME' does not exists. 'config'")

if not PRODUCTS_INFO_FILE_NAME:
    raise ValueError("Filename 'PRODUCTS_INFO_FILE_NAME' does not exists. 'config'")


