from django.contrib.auth.decorators import user_passes_test
def admin_test(user):
    if user.role == "Admin":
        return True
    else:
        return False
    
@user_passes_test(admin_test)
def admin_view(request):
    pass
