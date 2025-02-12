# In schemas.py

from pydantic import BaseModel
from typing import List, Optional

# Blog schema
class Blog(BaseModel):
    title: str
    body: str

# User schema for request
class User(BaseModel):
    name: str
    email: str
    password: str


# User schema for response
class ShowUser(BaseModel):
    name: str
    email: str
    # blogs: List[Optional[str]]  # List of blog titles, Optional because the user may have no blogs

    class Config:
        # orm_mode = True  # This allows SQLAlchemy models to be converted to Pydantic models
          from_attributes = True  # Updated for Pydantic V2

# Blog schema for response
class showBlog(BaseModel):
    title: str
    content: str
    # creator: ShowUser  # Nested ShowUser model for the creator

    class Config:
        # orm_mode = True  # This allows Pydantic to work with ORM models (like SQLAlchemy)
          from_attributes = True  # Updated for Pydantic V2


class Login(BaseModel):
    username: str  
    password: str



class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
