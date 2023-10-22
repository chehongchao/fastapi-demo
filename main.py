# 主应用入口
from core.logger_config import logger
from fastapi import FastAPI, HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

from api.api_v1.endpoints import items, login, users

app = FastAPI()


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.error(f"HTTPException occurred: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unexpected error occurred: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "An unexpected error occurred."},
    )


# 包含路由
app.include_router(items.router, prefix="/api/items", tags=["items"])
app.include_router(login.router, prefix="/api/login", tags=["login"])
app.include_router(users.router, prefix="/api/users", tags=["users"])


# 根路由
@app.get("/")
def read_root():
    return {"Hello": "World"}
