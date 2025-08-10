from django.urls import path
from .views import admin_view, librarian_view, member_view, register_view, list_books, LibraryDetailView

urlpatterns = [
    path('admin-zone/', admin_view, name='admin_view'),
    path('librarian-zone/', librarian_view, name='librarian_view'),
    path('member-zone/', member_view, name='member_view'),
    path('register/', register_view, name='register'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
