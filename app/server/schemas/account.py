from mongoengine import Document, StringField

class AccountSchema(Document):
    name: str     = StringField(required=True)
    email: str    = StringField(required=True)
    password: str = StringField(required=True)
