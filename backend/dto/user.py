from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    username: Optional[str]
    fullname: Optional[str]


class UserCreate(UserBase):
    username: str
    password: str


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class User(UserInDBBase):
    pass

# class UserInDB(UserInDBBase):
#     hashed_password: str
