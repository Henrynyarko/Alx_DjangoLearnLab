from django.shortcuts import render

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Book API!")
