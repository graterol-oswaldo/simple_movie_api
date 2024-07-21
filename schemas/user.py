from pydantic import BaseModel, Field
from typing import Optional



class UserBase(BaseModel):
    email:str = Field(min_length=8,max_length=150)
    password:str = Field(min_length=6,max_length=250)


class User(UserBase):
    name:str = Field(min_length=3, max_length=150)
    is_active: Optional[bool] = True
