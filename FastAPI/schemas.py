from pydantic import BaseModel
from typing import Optional

class ContactBase(BaseModel):
    firstname: str
    middlename: str
    lastname: str
    nickname: Optional[str] = None
    email: str
    phone: str
    phone_2: Optional[str] = None
    phone_3: Optional[str] = None
    address: Optional[str] = None
    relation: Optional[str] = None

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id: int

    class Config:
        orm_mode = True

class ContactUpdate(BaseModel):
    firstname: Optional[str] = None
    middlename: Optional[str] = None
    lastname: Optional[str] = None
    nickname: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    phone_2: Optional[str] = None
    phone_3: Optional[str] = None
    address: Optional[str] = None
    relation: Optional[str] = None
