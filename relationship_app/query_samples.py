import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="J.K. Rowling")
books_by_author = Book.objects.filter(author=author)
print("Books by J.K. Rowling:")
for book in books_by_author:
    print(f"- {book.title}")

# List all books in a library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print("\nBooks in Central Library:")
for book in books_in_library:
    print(f"- {book.title}")

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"\nLibrarian of Central Library: {librarian.name}")
