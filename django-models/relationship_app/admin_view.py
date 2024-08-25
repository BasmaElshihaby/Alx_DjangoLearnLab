from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def admin_test(user):
    if user.role == "Admin":
        return True
    else:
        return False
    
@user_passes_test(admin_test)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')
