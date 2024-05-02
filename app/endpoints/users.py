from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.core import get_db
from app.repositories import user_repository
from app.schemas.user_schema import UserCreate, UserUpdate

router = APIRouter()


@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = user_repository.get_user_by_username(db=db, username=user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    new_user = user_repository.create_user(db=db, username=user.username, email=user.email)
    return new_user


@router.put("/{user_id}")
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    existing_user = user_repository.get_user_by_id(db=db, user_id=user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user = user_repository.update_user(db=db, user=existing_user, username=user.username, email=user.email)
    return updated_user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    existing_user = user_repository.get_user_by_id(db=db, user_id=user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    user_repository.delete_user(db=db, user=existing_user)
    return existing_user
