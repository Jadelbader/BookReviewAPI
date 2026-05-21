# Book Review API

A RESTful API built using Django REST Framework (DRF) for managing books and reviews with JWT authentication.


# Features

- User Registration
- JWT Authentication
- Refresh Tokens
- Change Password
- List Books
- Book Details
- Add / Update / Delete Books (Admin Only)
- Add Reviews
- View Reviews
- Update/Delete Own Reviews

# Technologies Used

- Python 3
- Django
- Django REST Framework
- Simple JWT
- SQLite3

# Installation

## Clone the repository

```bash
git clone https://github.com/Jadelbader/BookReviewAPI.git
```

## Navigate to project folder

```bash
cd BookReviewAPI
```

## Create virtual environment

```bash
python -m venv venv
```

## Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## Install dependencies

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

## Run migrations

```bash
python manage.py migrate
```

## Create superuser

```bash
python manage.py createsuperuser
```

## Run server

```bash
python manage.py runserver
```

# Authentication

JWT Authentication is used in this project.

## Obtain Token

POST

```text
/api/token/
```

## Refresh Token

POST

```text
/api/token/refresh/
```

Authorization Header:

```text
Bearer <access_token>
```

---

# API Endpoints

## Authentication

- POST /api/register/
- POST /api/token/
- POST /api/token/refresh/
- PUT /api/change-password/

## Books

- GET /api/books/
- GET /api/books/<id>/
- POST /api/books/
- PUT /api/books/<id>/
- DELETE /api/books/<id>/

## Reviews

- POST /api/books/<book_id>/reviews/
- GET /api/books/<book_id>/reviews/
- PUT /api/reviews/<id>/
- DELETE /api/reviews/<id>/

# Testing

All endpoints were tested using Postman.


# Permissions

- Only authenticated users can add reviews.
- Users can only edit or delete their own reviews.
- Only admin users can create, update, or delete books.