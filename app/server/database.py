import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('MONGODB_USERNAME')
password = os.getenv('MONGODB_PASSWORD')

uri = f"mongodb+srv://{username}:{password}@cluster0.iee1y.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

try:
    client.admin.command('ping')
except Exception as e:
    print(e)

db = client.Yucode
menu_collection = db.get_collection('Menu')
