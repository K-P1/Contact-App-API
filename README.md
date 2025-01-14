# Contact Book API

## Overview
The Contact Book API is a simple and efficient tool to manage contact information. It provides CRUD functionality for managing contacts, along with search capabilities. The API has been implemented using both Django and FastAPI to suit different development preferences.

---

## Features
- Create, Read, Update, and Delete (CRUD) operations for contacts.
- Search functionality to filter contacts by name or phone number.
- Support for SQLite as the database backend.
- Swagger UI for testing endpoints (FastAPI).
- Optional Django templates for a user interface.

---

## Tech Stack
- **Backend Frameworks**: Django and FastAPI
- **Database**: SQLite (default, customizable)
- **Testing**: Manual and automated tests

---

## API Endpoints

### Common Endpoints
#### 1. Create a Contact
- **POST** `/contacts/`
- **Body**:
  ```json
  {
    "name": "John Doe",
    "phone_number": "1234567890",
    "email": "johndoe@example.com",
    "address": "123 Elm Street"
  }
  ```

#### 2. Retrieve All Contacts
- **GET** `/contacts/`

#### 3. Retrieve a Single Contact
- **GET** `/contacts/{id}/`

#### 4. Update a Contact
- **PUT** `/contacts/{id}/`
- **Body**:
  ```json
  {
    "name": "Jane Doe",
    "phone_number": "9876543210",
    "email": "janedoe@example.com",
    "address": "456 Maple Avenue"
  }
  ```

#### 5. Delete a Contact
- **DELETE** `/contacts/{id}/`

#### 6. Search Contacts
- **GET** `/contacts/search/?name=<name>&phone_number=<phone_number>`

---

## Setup Instructions

### Prerequisites
- Python 3.9+
- Virtual Environment (optional)

### Steps

#### 1. Clone the Repository
```bash
git clone <repository_url>
cd contact-book-api
```

#### 2. Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Migrate the Database
```bash
# For Django
python manage.py migrate

# For FastAPI (if using a database setup script)
python db_setup.py
```

#### 5. Run the Server
- **Django**:
  ```bash
  python manage.py runserver
  ```
- **FastAPI**:
  ```bash
  uvicorn main:app --reload
  ```

#### 6. Access the API
- Django: `http://127.0.0.1:8000/`
- FastAPI: `http://127.0.0.1:8000/docs` (Swagger UI)

---

## Testing

### Manual Testing
- Use tools like Postman or curl to test API endpoints.

### Automated Testing
- **Django**: Use the built-in test client.
  ```bash
  python manage.py test
  ```
- **FastAPI**: Use `pytest`.
  ```bash
  pytest
  ```

---

## Future Enhancements
- Add user authentication and authorization.
- Implement pagination for large datasets.
- Enhance search functionality with fuzzy matching.
