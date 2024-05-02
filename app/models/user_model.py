from sqlalchemy import Column, Integer, String
from app.core.database import Base


class UserModel(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)
    username: str = Column(String, index=True)
    email: str = Column(String, index=True)
