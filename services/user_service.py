# 用户相关的业务逻辑

from sqlalchemy.orm import Session

from core.security import get_password_hash
from db.models import User


# 获取用户列表
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()


# 根据用户名获取用户
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


# 创建新用户
def create_user(db: Session, user: dict):
    user["hashed_password"] = get_password_hash(user["password"])
    db_user = User(**user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
