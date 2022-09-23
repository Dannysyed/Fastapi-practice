from scheme import userShown,userType,user
from fastapi import FastAPI,Depends,APIRouter
from sqlalchemy.orm import Session
from fastapi.params import Body
from database import get_db
import models

router=APIRouter()

@router.post('/users')
def create_user(payload:user,db:Session=Depends(get_db)):
   data= models.User(**payload.dict())
   db.add(data)
   db.commit()
   db.refresh(data)
   return{'data':data}


@router.get('/users')
def get_user(db:Session=Depends(get_db)):
   data= db.query(models.User).all()
   return{"data":data}


    