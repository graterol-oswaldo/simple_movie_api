from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
from utils.jwt_manager import validate_token


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data: dict = validate_token(auth.credentials)
        if data["email"] != "admin@mymovieapi.lcl":
            raise HTTPException(status_code=403, detail="Invalid credentials")