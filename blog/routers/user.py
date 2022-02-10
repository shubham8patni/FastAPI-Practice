from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session
from ..hashing import Hash

router = APIRouter(tags=['Users']) 

@router.post('/user', status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User,db: Session = Depends(database.get_db)):
    new_user = models.User(name = request.name, age = request.age, email = request.email, password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/user', response_model=List[schemas.ShowUser])
def show_all_users(db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    return users

@router.get('/user/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User with id {id} is not available")
    return user