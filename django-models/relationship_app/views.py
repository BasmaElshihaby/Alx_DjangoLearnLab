from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login

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

def register(request):
    form = UserCreationForm(request.POST or None)
    
    # Check if the form is valid when submitted
    if form.is_valid():
        user = form.save()
        
        # Optionally log the user in after registration
        login(request, user)
        
        # Redirect to the login page upon successful registration
        return redirect(reverse_lazy('login'))
    
    # Render the registration form template
    return render(request, 'relationship_app/register.html', {'form': form})