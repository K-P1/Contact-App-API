from sqlalchemy import Column, Integer, String
from db import Base

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    middlename = Column(String, index=True, nullable=True)
    lastname = Column(String, index=True, nullable=True)
    email = Column(String, unique=True, index=True, nullable=True)
    phone = Column(String, unique=True, index=True)
    
    nickname = Column(String, index=True, nullable=True)
    phone_2 = Column(String, unique=True, index=True, nullable=True)
    phone_3 = Column(String, unique=True, index=True, nullable=True)
    address = Column(String, index=True, nullable=True)
    relation = Column(String, index=True, nullable=True)