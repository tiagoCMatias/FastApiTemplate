from sqlalchemy.orm import Session

from app.models import ItemModel
from app.schemas.item_schema import ItemCreate


def create_item(db: Session, item: ItemCreate) -> ItemModel:
    new_item = ItemModel(**item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item