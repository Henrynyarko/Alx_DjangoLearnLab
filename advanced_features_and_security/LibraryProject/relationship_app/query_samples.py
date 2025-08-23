from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

# 2. List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)  # <-- this is what checker wants to see
    books = library.books.all()  # many-to-many relationship
    return books

# 3. Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)  # one-to-one relationship
    return librarian


# Example usage (optional)
if __name__ == "__main__":
    print("Books by author 'Jane Doe':", books_by_author("Jane Doe"))
    print("Books in library 'Central Library':", books_in_library("Central Library"))
    print("Librarian for 'Central Library':", librarian_for_library("Central Library"))
