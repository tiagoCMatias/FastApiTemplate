from sqlalchemy import Column, Integer, String, Double
from sqlalchemy.orm import Mapped
from app.core.database import Base


class ItemModel(Base):
    __tablename__ = "items"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    name: Mapped[str] = Column(String)
    price: Mapped[float] = Column(Double)
    brand: Mapped[str] = Column(String, index=True)
    quantity: Mapped[int] = Column(Integer)
