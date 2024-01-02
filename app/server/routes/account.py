from fastapi import APIRouter
from bson.json_util import _json_convert, dumps
from server.models.account import add_account

router = APIRouter()

@router.get('/')
def get_account():
    account = add_account()
    print(dumps(account))
    return _json_convert(account)

@router.post('/')
def insert_account(account):
    print(account)
    return None
