from fastapi import APIRouter, Body, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.user import User, UserBase
from typing import Dict
from utils.jwt_manager import create_token
from sqlalchemy.orm import Session
from config.database import Base, engine
from services.user import UserService
from routers.main import get_db

user_router = APIRouter()


Base.metadata.create_all(bind=engine)


@user_router.post("/login", tags=["auth"], response_model=Dict, status_code=200)
def login(user_login: UserBase, db:Session=Depends(get_db)) -> Dict:
    user:User = UserService(db).get_user_by_email(user_login.email)
    if user.email == user_login.email and user.password == user_login.password:
        token: str = create_token(user.to_dict())
        return JSONResponse(content=token, status_code=200)
    return JSONResponse(content={"msg": "Invalid username or password"}, status_code=401)


@user_router.get("/users", tags=["users"], response_model=Dict, status_code=200)
def get_user_by_email(email: str, db: Session = Depends(get_db)) -> Dict:
    result = UserService(db).get_user_by_email(email)
    if not result:
        return JSONResponse(content={"msg": f"There is no any user record with the email: {email}"}, status_code=200)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@user_router.post("/users", tags=["users"], response_model=Dict, status_code=200)
def create_user(user: User = Body(), db: Session = Depends(get_db)) -> Dict:
    UserService(db).create_user(user)
    return JSONResponse(content={"msg": "The user was created"}, status_code=201)


@user_router.put("/users", tags=["users"], response_model=Dict, status_code=200)
def edit_user(email: str, user: User = Body(), db: Session = Depends(get_db)) -> Dict:
    result = UserService(db).get_user_by_email(email)
    if not result:
        return JSONResponse(content={"msg": f"There is no any user record with the email: {email}"}, status_code=200)
    UserService(db).update_user(email)
    return JSONResponse(content={"msg": "The user was updated"}, status_code=201)
