from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def Member_test(user):
    if user.role == "Member":
        return True
    else:
        return False
    
@user_passes_test(Member_test)
def Member_view(request):
    pass


