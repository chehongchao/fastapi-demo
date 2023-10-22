# 依赖工具函数
from db.session import SessionLocal


# 获取数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
