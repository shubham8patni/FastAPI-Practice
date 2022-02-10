import email
from typing import List, Optional
from pydantic import BaseModel

from blog.database import Base
 
class Blog(BaseModel):
    title:str
    body:str

class User(BaseModel):
    name: str
    age: int
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    age: int
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config():
        orm_mode = True

class Login(BaseModel):
    email: str
    password: str
    class Config():
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
