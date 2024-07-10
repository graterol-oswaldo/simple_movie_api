from pydantic import BaseModel, Field
from datetime import datetime
from random import choices
from string import ascii_letters, digits
from typing import Optional


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=1, max_length=50)
    overview: str = Field(min_length=1, max_length=300)
    year: int = Field(ge=1888, le=datetime.now().year)
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_length=1, max_length=50)

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "title": "Roundhay Garden Scene",
                "overview": "The first movie film ever recorded",
                "year": 1888,
                "rating": 10,
                "category": "Micro"
            }
        }}


data: list[dict] = [
    # {
    #     "id": 1,
    #     "title": "Avatar",
    #     "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
    #     "year": "2009",
    #     "rating": 7.8,
    #     "category": "Acción",
    # },
    # {
    #     "id": 2,
    #     "title": "Avatar",
    #     "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
    #     "year": "2009",
    #     "rating": 7.8,
    #     "category": "Acción",
    # },
]


movies: list[Movie] = [Movie(**item) for item in data]


def generate_random_string(lenght:int) -> str:
    characters:str = ascii_letters + digits
    return ''.join(choices(characters, k=lenght))

