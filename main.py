from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from fastapi.params import Body
import models
from scheme import userType,userShown
from database import engine,get_db
from  routes import posts,users,auth
app=FastAPI()
models.Base.metadata.create_all(bind=engine)

# Routes
@app.get('/')
def root():
    return {"message":"hello"}
# app.add_api_route(posts.APIRouter)
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)

