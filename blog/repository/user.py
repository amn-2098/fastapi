# In repository/user.py

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models, schemas
from ..hashing import Hash 

def create_user(request: schemas.User, db: Session):
    # Check if the user already exists based on email (or any unique identifier)
    existing_user = db.query(models.User).filter(models.User.email == request.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )

    # Hash the password before saving it
    hashed_password = Hash.bcrypt(request.password)

    # Create a new user with the hashed password
    new_user = models.User(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # Return the Pydantic model with name and email (no password)
    return schemas.ShowUser(name=new_user.name, email=new_user.email)

def get_user_by_id(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return schemas.ShowUser(name=user.name, email=user.email)  # Return Pydantic model
