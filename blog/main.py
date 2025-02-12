# In main.py

from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user
from .routers import login


app = FastAPI()

# Create all tables in the database if they don’t already exist.
models.Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(login.router)


# for route in app.routes:
#     print(f"📌 {route.path} → {route.methods}")
