# serializers.py
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Serialize all fields of the Book model

    def validate_published_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("The publication date cannot be in the future.")
        return value
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Serialize all fields of the Book model
    def get_related_books(self, obj):
        related_books = obj.related_books.all()  # Get all related books
        return BookSerializer(related_books, many=True).data 
