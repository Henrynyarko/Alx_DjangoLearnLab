from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# 📘 ListView - Anyone can see all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # ✅ public access


# 🔍 DetailView - Anyone can see a single book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # ✅ public access


# 🆕 CreateView - Only logged-in users can add
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # 🔐 only auth users


# ✏️ UpdateView - Only logged-in users can update
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # 🔐 only auth users


# ❌ DeleteView - Only logged-in users can delete
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # 🔐 only auth users

# Create your views here.


# Create your views here.
