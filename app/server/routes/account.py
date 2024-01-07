from fastapi import APIRouter, Response
from server.models.account import AccountSchema

router = APIRouter()

@router.post('/')
def account_root(account: AccountSchema):
    return Response(account.json(), media_type="application/json")