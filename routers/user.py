from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from crud import user as crud
from schemas import user as schemas
from core.database import get_db
from core.auth import create_jwt_token

router = APIRouter()

@router.post("/user/register")
def register(user: schemas.UserIn, db: Session = Depends(get_db)):
    existing_user = crud.get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Usuário já existe")
    
    new_user = crud.create_user(db, user.username, user.password)
    return {"message": "Usuário registrado com sucesso"}

@router.post("/user/login", response_model=schemas.Token)
def login(user: schemas.UserIn, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, user.username)
    if not db_user or not crud.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    
    token = create_jwt_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
