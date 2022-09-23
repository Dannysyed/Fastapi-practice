from scheme import userShown,userType,user
from fastapi import FastAPI,Depends,APIRouter,HTTPException,status
from sqlalchemy.orm import Session
from fastapi.params import Body
from database import get_db
import models
from oauth import create_access_token

router=APIRouter()

@router.get('/login')
def login(payload:user,db:Session=Depends(get_db)):
    email=db.query(models.User).filter(models.User.email==payload.email).first()
    if email is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    toekn=create_access_token({'userid':email.id})
    return{'data':toekn }


        
    