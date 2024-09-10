from fastapi import FastAPI, HTTPException, status, Query, Response, Depends
from pydantic import BaseModel
from typing import Optional
from random import randrange
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = FastAPI()
# Connect my SQL database to FastAPI
DATABASE_URL = "mysql+pymysql://root:password@localhost/bookexchange"

engine = create_engine(DATABASE_URL) # Connects FastAPI to mySQL

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine) # Used for creating a database session

Base =declarative_base() # Used to create SQLAlchemy models
