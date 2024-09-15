from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django_filters import rest_framework

#filters.OrderingFilter
#filters.SearchFilter
# ListView: Retrieve all books (GET)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# DetailView: Retrieve a single book by ID (GET)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# CreateView: Add a new book (POST)
# views.py

# CreateView: Add a new book (POST)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] 
    # Override perform_create to handle custom validation or additional logic
    def perform_create(self, serializer):
        # Custom validation (for example: ensure unique ISBN)
        isbn = serializer.validated_data.get('isbn')
        if Book.objects.filter(isbn=isbn).exists():
            raise ValidationError({'isbn': 'A book with this ISBN already exists.'})

        # Call save() on the serializer to create the new book
        serializer.save()

    # Optionally, override create method to customize the response
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Perform creation
        self.perform_create(serializer)

        # Customize the response after book creation
        headers = self.get_success_headers(serializer.data)
        return Response({
            'message': 'Book created successfully!',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED, headers=headers)


# UpdateView: Modify an existing book (PUT/PATCH)


# UpdateView: Modify an existing book (PUT/PATCH)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update
    # Override perform_update to handle custom validation
    def perform_update(self, serializer):
        # Custom validation (for example: ensure unique ISBN for updates)
        isbn = serializer.validated_data.get('isbn')
        book_id = self.get_object().id  # Get the current book ID

        # Ensure that no other book with the same ISBN exists
        if Book.objects.filter(isbn=isbn).exclude(id=book_id).exists():
            raise ValidationError({'isbn': 'Another book with this ISBN already exists.'})

        # Call save() on the serializer to update the book
        serializer.save()

    # Optionally, override update method to customize the response
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        # Perform the update
        self.perform_update(serializer)

        # Customize the response after book update
        return Response({
            'message': 'Book updated successfully!',
            'data': serializer.data
        }, status=status.HTTP_200_OK)


# DeleteView: Remove a book (DELETE)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete
