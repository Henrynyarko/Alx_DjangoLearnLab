from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book, Library
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Library, Book   # <--- this line is good. But if needed, split it:
from .models import Library  # <-- Make sure this line is literally there

# from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library

# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
