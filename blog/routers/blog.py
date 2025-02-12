# In routers/blog.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database,oauth2
from ..repository import blog
from ..schemas import ShowUser

get_db = database.get_db

router = APIRouter(
    prefix="/blog",  # Prefix for all the routes in this router
    tags=["Blogs"]
)

# CREATE BLOG
@router.post("/", status_code=status.HTTP_201_CREATED ,response_model=ShowUser)
def create(request: schemas.Blog, db: Session = Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)  # Should return Pydantic model

# DELETE BLOG
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)  # Should return a message in dict form

# UPDATE BLOG
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)  # Should return Pydantic model

# GET ALL BLOGS
@router.get("", response_model=List[schemas.showBlog])  # Here, List[schemas.showBlog] should be used
def get_all_blogs(db: Session = Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)  # Should return List of Pydantic models

# GET SINGLE BLOG
@router.get("/{id}", status_code=200, response_model=schemas.showBlog)
def show(id: int, db: Session = Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)  # Should return Pydantic model



