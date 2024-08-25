from bookshelf.models import Book
Book.objects.get(pk=1).title
# '1984'

Book.objects.get(pk=1).author
# 'George Orwell'

Book.objects.get(pk=1).publication_year
# 1949