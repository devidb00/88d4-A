from fastapi import APIRouter

router = APIRouter()

@router.post('/')
def get_account():
    return { "msg": "No user find !" }