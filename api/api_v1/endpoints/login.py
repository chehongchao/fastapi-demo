from fastapi import APIRouter, HTTPException

from core.security import verify_password, create_access_token
from services.user_service import get_user_by_username

router = APIRouter()


# 用户登录
@router.post("/login/")
def login_user(username: str, password: str):
    user = get_user_by_username(username)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="用户名或密码错误")
    access_token = create_access_token(data={"sub": username})
    return {"access_token": access_token, "token_type": "bearer"}
