from mongoengine import connect

class MongoDB:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.uri = f"mongodb+srv://{self.username}:{self.password}@cluster0.iee1y.mongodb.net/?retryWrites=true&w=majority"

    def connect_db(self, database):
        return connect(host=f'{self.uri}/{database}')