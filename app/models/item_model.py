from sqlalchemy import Column, Integer, String, Double
from app.core.database import Base


class ItemModel(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Double)
    brand = Column(String, index=True)
    quantity = Column(Integer)
