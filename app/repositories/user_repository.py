from sqlalchemy.orm import Session
from app.models import UserModel


def get_user_by_username(db: Session, username: str):
    return db.query(UserModel).filter(UserModel.username == username).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def create_user(db: Session, username: str, email: str):
    new_user = UserModel(username=username, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update_user(db: Session, user: UserModel, username: str, email: str):
    user.username = username
    user.email = email
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user: UserModel):
    db.delete(user)
    db.commit()
    return user
