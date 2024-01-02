from server.database import database

collection = database.get_collection('Menu')

def add_account():
    return collection.find_one()