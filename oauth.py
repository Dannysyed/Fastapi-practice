from jose import JWTError,jwt
from datetime import datetime,timedelta
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
# from scheme import TokenData
from sqlalchemy.orm import Session
from database import get_db
from fastapi.security import OAuth2PasswordBearer
import models
oauth2_scheme=OAuth2PasswordBearer(tokenUrl='login')
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

 
def create_access_token(token:dict):
    data_token=token.copy()
    expire=datetime.now()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data_token.update({'exp':expire})
    encoded_jwt=jwt.encode(data_token,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token,crendtial_expen):
  decoded=  jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
  id=decoded.get('userid')
  if id is None:
      raise crendtial_expen
  return id

def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):
    credentail_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f'could not validate credentials',headers={"WWW-Authenicate":"Bearer"})
    
    user_id=verify_token(token,credentail_exception)
    data=db.query(models.User).filter(models.User.id==user_id).first()
    print(user_id,'****',data)
    return data