from .models import *

Book.objects.filter(author=1)

Book.objects.filter(books=1)

Library.objects.get(pk=1).librarian