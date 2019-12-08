from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import Book
from book.serializers import BookListSerializer


class BookAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer


class BookCreateAPIView(CreateAPIView):
    serializer_class = BookListSerializer


class BookUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
