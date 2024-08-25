from .models import *

author_name = "Ahmed"
author = Author.objects.get(name=author_name)
Book.objects.filter(author=author)

books = Book.objects
books.all()

library_name = "First library"
Library.objects.get(name=library_name)

Librarian.objects.get(library=library_name)