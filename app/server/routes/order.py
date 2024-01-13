from fastapi import APIRouter, Response

router = APIRouter()

@router.get('/')
def get_order():
    return Response(status_code=204)