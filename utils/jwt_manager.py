from jwt import encode, decode
from typing import Dict
import os




def create_token(data: dict) -> str:
    jwt_token: str = encode(
        payload=data, key=os.getenv("JWT_SECRET", "MY_SECRET_KEY"), algorithm="HS256")
    return jwt_token


def validate_token(jwt_token: str) -> Dict:
    data: dict = decode(jwt_token, key=os.getenv("JWT_SECRET", "MY_SECRET_KEY"), algorithms=['HS256'])
    return data
