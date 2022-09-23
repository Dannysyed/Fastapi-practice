from pydantic import BaseModel
class userType(BaseModel):
    title:str
    content:str
    
class userShown(BaseModel):
    title:str
    
class user(BaseModel):
    email:str
    password:str
    

