import uvicorn
from fastapi import FastAPI, APIRouter

from api.handlers import router_test

app = FastAPI()

main_api_router = APIRouter()

main_api_router.include_router(router_test)

app.include_router(main_api_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
