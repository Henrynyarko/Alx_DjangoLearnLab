from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),  # ✅ Must be views.register
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('admin-zone/', views.admin_view, name='admin_view'),
    path('librarian-zone/', views.librarian_view, name='librarian_view'),
    path('member-zone/', views.member_view, name='member_view'),
]

from .views import admin_view, librarian_view, member_view

urlpatterns += [
    path('admin-role/', admin_view, name='admin_view'),
    path('librarian-role/', librarian_view, name='librarian_view'),
    path('member-role/', member_view, name='member_view'),
]
