from .models import *

Book.objects.filter(author=1)

books = Book.objects
books.all()

library_name = "First library"
Library.objects.get(name=library_name)