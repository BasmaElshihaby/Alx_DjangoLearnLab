from .models import *
author_name = "Ahmed"
Author.objects.get(name=author_name)

books = Book.objects
books.all()

library_name = "First library"
Library.objects.get(name=library_name)