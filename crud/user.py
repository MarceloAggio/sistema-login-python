from sqlalchemy.orm import Session
from models.user import User
from core.auth import hash_password, verify_password

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, username: str, password: str):
    hashed_pw = hash_password(password)
    db_user = User(username=username, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
