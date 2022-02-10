from fastapi import APIRouter, Depends, HTTPException, status
from ..hashing import Hash
from .. import database, schemas, models, JWTtoken
from sqlalchemy.orm import Session

router = APIRouter(
    tags=['Login']
)



@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"user with id {request.email} not found")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Incprrect Password")
    
    access_token = JWTtoken.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}