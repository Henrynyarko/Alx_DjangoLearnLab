import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="J.K. Rowling")
books = Book.objects.filter(author=author)
print(f"Books by {author.name}:")
for book in books:
    print(book.title)

# List all books in a library
library = Library.objects.get(name="Central Library")
print(f"\nBooks in {library.name}:")
for book in library.books.all():
    print(book.title)

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"\nLibrarian for {library.name}: {librarian.name}")
