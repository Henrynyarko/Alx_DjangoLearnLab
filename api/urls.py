
from django.urls import path
from .views import BookListCreateView, home

urlpatterns = [
    path('', home, name='home'),
    path('books/', BookListCreateView.as_view(), name='book-list'),
]
