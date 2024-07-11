from jwt import encode, decode
from typing import Dict


def create_token(data: dict) -> str:
    jwt_token: str = encode(
        payload=data, key='my_secret_key', algorithm="HS256")
    return jwt_token


def validate_token(jwt_token: str) -> Dict:
    data: dict = decode(jwt_token, key='my_secret_key', algorithms=['HS256'])
    return data
