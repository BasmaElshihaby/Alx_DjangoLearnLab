
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def librarian_test(user):
    if user.role == "Librarian":
        return True
    else:
        return False
    
@user_passes_test(librarian_test)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')
