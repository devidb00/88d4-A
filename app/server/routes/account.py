from pydantic import BaseModel
from fastapi import APIRouter, Response
from server.models.account import find_account, insert_account

router = APIRouter()

class Account(BaseModel):
    name: str
    email: str
    password: str

@router.get('/')
def account_root(id: str):
    return Response(content=find_account(id), media_type="application/json", status_code=200)

@router.post('/')
def add_account(account: Account):
    insert_account(account.dict())
    return Response(status_code=204)