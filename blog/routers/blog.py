from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session

router = APIRouter(tags=['Blogs']) 


@router.get('/blog', response_model=List[schemas.ShowBlog])
def all_blog(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.post('/blog', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(database.get_db)):
    new_blog = models.Blog(title=request.title, body = request.body, user_id=1) #schema using model, we already have model use it
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog 


@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"blog with id {id} not found")
    blog.update(request.dict())
    db.commit()
    #return Response(status_code=status.HTTP_202_ACCEPTED) 


@router.delete('/blog/{id}', status_code = status.HTTP_202_ACCEPTED)
def destroy(id, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    db.refresh(blog)
    return {"status" : "Done"}

@router.get('/blog/{id}')
def get_id(id: int, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"blog with id {id} is not available")
        #return Response(status_code = status.HTTP_404_NOT_FOUND)
        #return {"detail" : f"blog with id {id} is not available"}
    return blog 