from scheme import userShown,userType
from fastapi import FastAPI,Depends,APIRouter
from sqlalchemy.orm import Session
from fastapi.params import Body
from database import get_db
import models
from oauth import get_current_user 
router=APIRouter()
@router.post('/posts',response_model=userShown)
def create_post(payload:userType,db:Session=Depends(get_db)):
    data= models.Posts(**payload.dict())
    print(data)
    db.add(data)
    db.commit()
    db.refresh(data)
    
    print(payload.dict())
    data=payload.dict()
    return data


@router.get('/posts')
def get_posts(db:Session=Depends(get_db),get_user:int=Depends(get_current_user)):
   print(get_user.email)
   data= db.query(models.Posts).all()
   return{"all_post":data}

@router.get('/posts/{idd}')
def get_post(idd,db:Session=Depends(get_db)):
    data=db.query(models.Posts).filter(models.Posts.id==idd).first()
    return{'post':data}