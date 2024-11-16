from sqlalchemy.orm import Session
from models import Contact
from schemas import ContactCreate, ContactUpdate

def create_contact(db: Session, contact: ContactCreate):
    db_contact = Contact(**contact.model_dump())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def get_contact(db: Session, id: str):
    id = id.strip()
    search_pattern = f"%{id}%"
    return db.query(Contact).filter(
        (Contact.firstname.ilike(search_pattern)) |
        (Contact.middlename.ilike(search_pattern)) |
        (Contact.lastname.ilike(search_pattern)) |
        (Contact.nickname.ilike(search_pattern)) |
        (Contact.phone.ilike(search_pattern)) |
        (Contact.phone_2.ilike(search_pattern)) |
        (Contact.phone_3.ilike(search_pattern)) |
        (Contact.email.ilike(search_pattern))
    ).first()

def get_all_contacts(db: Session):
    return db.query(Contact).all()

def update_contact(db: Session, contact: ContactUpdate, id: str):
    data= contact.model_dump(exclude_unset=True)
    db_contact = get_contact(db=db, id=id)
    if db_contact:
        for key, value in data.items():
            setattr(db_contact, key, value)
        db.commit()
        db.refresh(db_contact)
        return db_contact
    return None

def delete_contact(db: Session, id: str):
    db_contact = get_contact(db=db, id=id)
    if db_contact:
        db.delete(db_contact)
        db.commit()
        return db_contact
    return None
