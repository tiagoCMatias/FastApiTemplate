from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr


class UserUpdate(BaseModel):
    username: str
    email: EmailStr


class UserDelete(BaseModel):
    username: str
