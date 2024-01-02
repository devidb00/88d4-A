from pymongo import MongoClient

class MongoDB:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.uri = f"mongodb+srv://{self.username}:{self.password}@cluster0.iee1y.mongodb.net/?retryWrites=true&w=majority"

    def connect(self):
        return MongoClient(self.uri)
    
    def test_connection(self):
        try:
            MongoClient(self.uri).admin.command('ping')
            print('Successfully pinged !')
        except Exception as e:
            print(e)

