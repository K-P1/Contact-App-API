from fastapi import FastAPI, Depends, HTTPException, Path
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db import SessionLocal, Base, engine
from schemas import ContactCreate, ContactUpdate, Contact as ContactSchema
from crud import create_contact, get_contact, get_all_contacts, update_contact, delete_contact

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/create_contact', response_model=ContactSchema)
async def create_contact_endpoint(contact: ContactCreate, db: Session = Depends(get_db)):
    created_contact = create_contact(db=db, contact=contact)
    if not created_contact:
        raise HTTPException(status_code=500, detail="Failed to create contact")
    return JSONResponse(status_code=201, content={"detail": "Contact created successfully"})

@app.get('/get_contact/{id}', response_model=ContactUpdate)
async def get_contact_endpoint(
    id: str = Path(
        ..., 
        description="The Phone number or name of the contact to retrieve"), 
        db: Session = Depends(get_db)):
    contact = get_contact(db=db, id=id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@app.get('/get_all_contacts', response_model=list[ContactUpdate])
async def get_all_contacts_endpoint(db: Session = Depends(get_db)):
    contacts = get_all_contacts(db=db)
    if contacts is None:
        raise HTTPException(status_code=404, detail="No contacts found")
    return contacts

@app.patch('/update_contact/{id}', response_model=ContactUpdate)
async def update_contact_endpoint(
    contact: ContactUpdate, 
    id: str = Path(..., description="The Phone number or name of the contact to retrieve"), 
    db: Session = Depends(get_db)):
    
    updated_contact = update_contact(db=db, contact=contact, id=id)
    if not updated_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return JSONResponse(status_code=200, content={"detail": "Contact updated successfully"})

@app.delete('/delete_contact/{id}', response_model=ContactUpdate)
async def delete_contact_endpoint(
    id: str = Path(..., description="The Phone number or name of the contact to retrieve"),
    db: Session = Depends(get_db)):
    deleted_contact = delete_contact(db=db, id=id)
    if not deleted_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return JSONResponse(status_code=200, content={"detail": "Contact deleted successfully"})