from fastapi import APIRouter

router = APIRouter()


@router.post('/')
def get_user(user):
    return { "msg": "No user find !" }
