from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from api.deps import get_db
from services.item_service import get_items, create_item

router = APIRouter()


# 获取物品列表
@router.get("/items/", response_model=List[dict])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = get_items(db, skip=skip, limit=limit)
    return items


# 创建新物品
@router.post("/items/")
def create_new_item(item: dict, db: Session = Depends(get_db)):
    return create_item(db, item)
