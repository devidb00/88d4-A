from typing import Optional
from pydantic import BaseModel
from fastapi import APIRouter, Response
from server.schemas.account import AccountSchema

router = APIRouter()

class Account(BaseModel):
    name: str
    email: str
    password: str
    e: str = None

@router.post('/')
def account_root(data: Account):
    print(data)
    return Response("Text", media_type="application/json")