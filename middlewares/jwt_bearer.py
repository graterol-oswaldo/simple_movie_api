from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer
from utils.jwt_manager import validate_token
from services.user import UserService
from schemas.user import User
from sqlalchemy.orm import Session
from services.user import UserService
from routers.main import get_db



class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request, db:Session=Depends(get_db)):
        auth = await super().__call__(request)
        data: dict = validate_token(auth.credentials)
        user:User = UserService(db).get_user_by_email(data["email"])
        if not user:        
            raise HTTPException(status_code=403, detail="Invalid credentials")