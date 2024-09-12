from pydantic import BaseModel, EmailStr, Field
from models import Base
from datetime import datetime
import database
# Creating pydantic models. They are used for data validation.

class Profile(BaseModel):
    user_id: int
    username: str
    email: str
    password: str
    location: str
    profile_picture: str
    is_active: bool
    books_exchanged: int
    created_at: datetime = datetime.now()

    class Config:
        orm_mode = True
    
class Books(BaseModel):
    book_id:int
    title:str
    author:str
    genre:str
    description:str
    image:str
    user_id: int
    availability:bool

    class Config:
        orm_mode = True
    
class Exchange(BaseModel):
    book_id: int
    requester_id: int
    owner_id: int
    request_id: int
    status: str

    class Config:
        orm_mode = True

class Reviews(BaseModel):
    reviewer_id: int
    reviewee_id: int
    exchange_id: int
    review_id: int
    review: str
    rating: int
    comments: str

    class Config:
        orm_mode = True