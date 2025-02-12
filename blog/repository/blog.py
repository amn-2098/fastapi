# In repository/blog.py

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models, schemas

# Function to get all blogs
def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return [schemas.showBlog(title=blog.title, content=blog.body) for blog in blogs]

# Function to create a new blog
def create(request, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)  # user_id is hardcoded for now
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog) 
    return schemas.showBlog(title=new_blog.title, content=new_blog.body)  # Return Pydantic model

# Function to delete a blog by ID
def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    db.delete(blog)
    db.commit()
    return {"message": "Blog deleted successfully"}

# Function to update a blog by ID
def update(id: int, request, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    blog.title = request.title
    blog.body = request.body
    db.commit()
    db.refresh(blog)
    return schemas.showBlog(title=blog.title, content=blog.body)  # Return Pydantic model

# Function to get a blog by ID
def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return schemas.showBlog(title=blog.title, content=blog.body)  # Return Pydantic model
