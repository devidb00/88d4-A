import os
from dotenv import load_dotenv

from pymongo import MongoClient

load_dotenv()

class MongoDB:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.uri = f"mongodb+srv://{self.username}:{self.password}@cluster0.iee1y.mongodb.net/?retryWrites=true&w=majority"

    def connect(self, database):
        return MongoClient(self.uri).get_database(database)
    
    def test_connection(self):
        try:
            MongoClient(self.uri).admin.command('ping')
            print('Successfully pinged !')
        except Exception as e:
            print(e)



# Database connection
db_name = os.getenv('MONGODB_NAME')
db_username = os.getenv('MONGODB_USERNAME')
db_password = os.getenv('MONGODB_PASSWORD')
database = MongoDB(db_username, db_password).connect(db_name)