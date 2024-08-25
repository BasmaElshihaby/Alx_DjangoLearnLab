from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library


# Create your views here.
def list_books(request):
      
      books = Book.objects.all()
      context = {'books': books}
      return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Get default context data
        id = self.kwargs.get('pk')

        library = Library.objects.get(pk=id) # Retrieve the current book instance
        context['library'] = library
        return context