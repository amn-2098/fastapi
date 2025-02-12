
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models, database, hashing
from ..repository import user  # Import the user repository

get_db = database.get_db

router = APIRouter(
    prefix="/user",  # prefix added to all routes in this router
    tags=["Users"]
)

# CREATING USER
@router.post('', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)  # Call the create_user function from the repository

# GETTING USER
@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user_by_id(id, db)  # Call the get_user_by_id function from the repository
