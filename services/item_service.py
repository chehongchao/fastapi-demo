# 物品相关的业务逻辑

from sqlalchemy.orm import Session

from db.models import Item


# 获取物品列表
def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Item).offset(skip).limit(limit).all()


# 创建新物品
def create_item(db: Session, item: dict):
    db_item = Item(**item)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
