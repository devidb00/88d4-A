from bson.json_util import dumps
from bson.objectid import ObjectId
from server.database import mongodb_db

def find_account(id):
    collection = mongodb_db.db.get_collection('Menu')
    return dumps(collection.find({ '_id': ObjectId(id) }))

def insert_account(account):
    collection = mongodb_db.db.get_collection('Menu')
    collection.insert_one(account)
