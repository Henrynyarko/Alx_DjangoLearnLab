from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList  # assuming BookList already exists

# Create a router and register our viewset
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing view (optional if still needed)
    path('books/', BookList.as_view(), name='book-list'),

    # Add router-generated routes
    path('', include(router.urls)),
]
