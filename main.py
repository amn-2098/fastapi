
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app =  FastAPI()

# @app.get('/')  # Handles GET requests
# def index():
#     return {"data" :"blog list"}


'''Query Parameter(?)'''

@app.get('/blog') 
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None): 
    if published:
        # Only get a limited number of published blogs
        return {"data": f"{limit} published blogs from the database"}
    else:
        return {"data": f"{limit} blogs from the database"}



@app.get("/about")
def about():
    return {"message":"hello!, About"}



''' Static Route(first)'''

@app.get("/blog/unpublished") # Static Route 
def unpublished():
    # Fetching all unpublished blogs
    return {"data": "all unpublished blogs"}


'''# Dynamic Route(Second)'''

@app.get("/blog/{id}")   # {id} is a path parameter
def show(id: int):  # Define id as an integer
    #fetch blog with id = id 
    return {"data" : id}



@app.get("/blog/{id}/comments")
def comments(id):
    #fetch comments of blog with id = id
    return {"data" : {'1','2'}}



''' REQUEST BODY '''

# Define Blog model using Pydantic's BaseModel
class Blog(BaseModel):
    title: str  # Required field
    content: str  # Required field
    published: bool = True  # Optional field with default value

# Create a new blog using POST method
@app.post("/blog")
def create_blog(blog: Blog):  #ensures incoming data follows Blog model.
    return {"message": f"Blog is created with title: {blog.title}"} # Confirms blog creation with the provided title

