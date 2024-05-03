from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped

from app.core.database import Base


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    username: Mapped[str] = Column(String, index=True)
    email: Mapped[str] = Column(String, index=True)
