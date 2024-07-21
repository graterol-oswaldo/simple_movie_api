from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class Movie(BaseModel):
    title: str = Field(min_length=1, max_length=50)
    overview: str = Field(min_length=1, max_length=300)
    year: int = Field(ge=1888, le=datetime.now().year)
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_length=1, max_length=50)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Roundhay Garden Scene",
                "overview": "The first movie film ever recorded",
                "year": 1888,
                "rating": 10,
                "category": "Micro"
            }
        }}
