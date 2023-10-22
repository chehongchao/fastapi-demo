from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from api.deps import get_db
from services.user_service import get_users, create_user

router = APIRouter()


# 获取用户列表
@router.get("/users/", response_model=List[dict])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


# 创建新用户
@router.post("/users/")
def create_new_user(user: dict, db: Session = Depends(get_db)):
    return create_user(db, user)
