from fastapi import APIRouter, HTTPException, Depends
from core.auth import verify_jwt_token
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

@router.get("/protected")
def protected_route(token: str = Depends(oauth2_scheme)):
    payload = verify_jwt_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")
    
    return {"message": f"Acesso permitido para {payload['sub']}"}
