from .models import *

Book.objects.filter(author=1)

Book.objects.filter(books=1)

library_name = "First library"
Library.objects.get(name=library_name)