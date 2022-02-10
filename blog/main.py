from turtle import title
from typing import List
from urllib import response
from fastapi import FastAPI, Depends, status, HTTPException, Response 
import uvicorn

from blog.routers import authentication, user
from .database import engine, get_db
from . import schemas, models
from sqlalchemy.orm import Session
from .hashing import Hash
from .routers import blog, user, authentication


app = FastAPI()
 
models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close

# @app.delete('/blog/{id}', status_code = status.HTTP_202_ACCEPTED, tags=['Blogs'])
# def destroy(id, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"blog with id {id} not found")
#     blog.delete(synchronize_session=False)
#     db.commit()
#     db.refresh(blog)
#     return {"status" : "Done"}

# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['Blogs'])
# def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"blog with id {id} not found")
#     blog.update(request.dict())
#     db.commit()
#     #return Response(status_code=status.HTTP_202_ACCEPTED) 

# @app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['Blogs'])
# def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title, body = request.body, user_id=1) #schema using model, we already have model use it
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog 


# @app.get('/blog', response_model=List[schemas.ShowBlog], tags=['Blogs'])
# def all_blog(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs


# @app.get('/blog/{id}', tags=['Blogs'])
# def get_id(id: int, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"blog with id {id} is not available")
#         #return Response(status_code = status.HTTP_404_NOT_FOUND)
#         #return {"detail" : f"blog with id {id} is not available"}
#     return blog 




# @app.post('/user', status_code=status.HTTP_201_CREATED, tags=['Users'])
# def create_user(request: schemas.User,db: Session = Depends(get_db)):
#     new_user = models.User(name = request.name, age = request.age, email = request.email, password = Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user', response_model=List[schemas.ShowUser], tags=['Users'])
# def show_all_users(db: Session = Depends(get_db)):
#     users = db.query(models.User).all()
#     return users

# @app.get('/user/{id}', response_model=schemas.ShowUser, tags=['Users'])
# def get_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User with id {id} is not available")
#     return user