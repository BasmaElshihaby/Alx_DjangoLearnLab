from bookshelf.models import Book
first_book = Book.objects.create(title="1984", author="George Orwell", production_year=1949)