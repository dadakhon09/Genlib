from abc import ABC

from rest_framework import serializers

from book.models import Book, Author


class BookListSerializer(serializers.ModelSerializer, ):
    class Meta:
        model = Book
        fields = ('id', 'name', 'description', 'image', 'file')
