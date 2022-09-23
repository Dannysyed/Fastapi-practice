from database import Base
from sqlalchemy import String,Integer,Column,TIMESTAMP,text
class Posts(Base):
    __tablename__='Demo'
    id=Column(Integer,primary_key=True,nullable=False)
    title=Column(String,nullable=False)
    content=Column(String,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

class User(Base):
    __tablename__="Demousers"
    id=Column(Integer,primary_key=True,nullable=False)
    email=Column(String,nullable=False)
    password=Column(String,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))