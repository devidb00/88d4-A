from server.app import database

collection = database.get_collection('Menu')

def insert_menu(user):
    collection.insert_one(user)