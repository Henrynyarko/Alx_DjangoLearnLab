# API Views Overview

## Endpoints

- `GET /api/books/` — List all books (public)
- `GET /api/books/<id>/` — View one book (public)
- `POST /api/books/create/` — Add a new book (auth required)
- `PUT /api/books/<id>/update/` — Update book (auth required)
- `DELETE /api/books/<id>/delete/` — Delete book (auth required)

## Permissions

- `AllowAny` for read operations
- `IsAuthenticated` for write operations

## Custom Behavior

- Uses Django REST Framework Generic Views for CRUD operations
- Uses built-in permission classes
