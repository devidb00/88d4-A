from pymongo import MongoClient
from server.config import settings

class MongoDB:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.uri = f"mongodb+srv://{self.username}:{self.password}@cluster0.iee1y.mongodb.net/?retryWrites=true&w=majority"
        self.conn = None

    def connect_db(self, database):
        self.conn = MongoClient(f'{self.uri}')
        self.db = self.conn.get_database(database)

        return self.db
    
    def disconnect(self):
        self.conn.close()

db_username = settings.mongodb_username
db_password = settings.mongodb_password
mongodb_db = MongoDB(db_username, db_password)