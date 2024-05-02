from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core import get_db
from app.repositories import item_repository
from app.schemas.item_schema import ItemCreate

router = APIRouter()

@router.post("/")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    new_user = item_repository.create_item(db=db, item=item)
    return new_user
