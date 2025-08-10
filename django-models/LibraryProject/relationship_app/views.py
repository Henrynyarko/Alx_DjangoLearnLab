from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import DetailView
from django.contrib.auth.decorators import user_passes_test
from .models import Book, Library

# Role check helper function
def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

# Librarian-only view protected by role check
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Other existing views (optional, keep if you want)
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


def admin_view(request):
    # Placeholder admin view
    return render(request, 'relationship_app/admin_view.html')

def member_view(request):
    # Placeholder member view
    return render(request, 'relationship_app/member_view.html')
