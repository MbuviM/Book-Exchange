from pydantic import BaseModel
from models import Base
from datetime import datetime
# Creating pydantic models. They are used for data validation.

class UserBase(BaseModel):
    username:str
    email:str
    location:str
    profile_pic:str
    is_active:bool
    books_exchanged:int
    created_at:datetime = datetime.now()

class UserCreate(UserBase):
    pass

class User(UserBase):
    id:int
    is_active:bool
    
class BooksBase(BaseModel):
    id:int
    title:str
    author:str
    genre:str
    description:str
    image:str
    availability:bool
    added_at: datetime = datetime.now()

class BooksCreate(BooksBase):
    pass

class Books(BooksBase):
    id:int
    availability:bool
