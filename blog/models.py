from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  # Auto-incremented primary key
    name = Column(String)
    email = Column(String)
    password = Column(String)


    blogs = relationship("Blog", back_populates="creator")  # One-to-many relationship with Blog



class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)  # Auto-incremented primary key
    title = Column(String, index=True)  # Title column (required)
    body = Column(String)  # Body column (required)
    user_id = Column(Integer, ForeignKey('users.id'))  # Foreign key reference


    creator = relationship("User", back_populates="blogs")  # Many-to-one relationship with User





