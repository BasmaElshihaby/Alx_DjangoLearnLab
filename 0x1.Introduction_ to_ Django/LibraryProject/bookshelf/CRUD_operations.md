from bookshelf.models import Book
first_book = Book(title="1984", author="George Orwell", production_year=1949)
first_book.save()

from bookshelf.models import Book
Book.objects.get(pk=1).title
# '1984'

Book.objects.get(pk=1).author
# 'George Orwell'

Book.objects.get(pk=1).production_year
# 1949


from bookshelf.models import Book
first_book = Book.objects.get(pk=1)
first_book.title = "Nineteen Eighty-Four"
first_book.save()



from bookshelf.models import Book
first_book = Book.objects.get(pk=1)
first_book.delete()

Book.objects.all()
# <QuerySet []>
