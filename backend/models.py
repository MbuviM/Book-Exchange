from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from backend.database import Base

# index helps in faster retrieval of data
# User Table
class User (Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(Integer, index=True, unique=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, unique=True)
    location = Column(String)
    profile_pic = Column(String)
    is_active = Column(Boolean, default=True)
    books_exchanged = Column(Integer)


class Books(Base):

    __tablename__ = "books"
    book_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    genre = Column(String, index=True)
    description = Column(String(255))
    image = Column(String)
    user_id = ForeignKey("user_id")
    availability = Column(Boolean, default=True)

