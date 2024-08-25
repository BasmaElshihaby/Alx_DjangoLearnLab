from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view

urlpatterns = [
    path('books/', views.list_books, name='books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', admin_view, name='admin'),
    path('librarian/', librarian_view, name='librarian'),
    path('member/', member_view, name='member'),
]