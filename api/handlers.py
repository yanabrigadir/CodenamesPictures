from fastapi import APIRouter

router_test = APIRouter()

@router_test.get("/")
async def root():
    return {"message": "Hello World"}