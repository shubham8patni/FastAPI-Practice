from lib2to3.pytree import Base
import this
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn 

app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] 

@app.get('/')
def index():
    return {"data" : {"Name" : "hello world"}}

#binindg query parameters to url. similar to path values
@app.get('/blog')
def index(limit, published : bool): #url query parameters instead of path parameters (both are very similar)
    if published:
        return {"data" : {"Name" : f"{limit} published blog list"}} #without 'f' the "{limit}" value will not change 
    else:
        return {"data" : {"Name" : f"{limit} blog list"}}



@app.get('/about')
def about():
    return {"data" : {"name" : "about page"}}

@app.get('/blog/unpublished')
def unpublished():
    return {"data" : "all unpublished blogs"}
    
#dynamic url content
@app.get('/blog/{id}')
def blog(id: int): #id: int defining that id will always be integer or accepted as integer also provides good error message
    return {"data" : id}


#dynamic url binding content
@app.get('/blog/{id}/comments')
def comments(id):
    return {"data" : {'1' , '2'}} 


@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f"Blog is created with title as {request.title}"}

if __name__ == "__main__":

    uvicorn.run(app,host = "127.0.0.1", port = 9000)