from mongoengine import *

class AccountSchema(Document):
    name: str     = StringField(required=True)
    email: str    = StringField(required=True)
    password: str = StringField(required=True)
