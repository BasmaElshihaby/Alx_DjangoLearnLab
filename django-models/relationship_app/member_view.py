from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def member_test(user):
    if user.role == "Member":
        return True
    else:
        return False
    
@user_passes_test(member_test)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


