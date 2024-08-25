from django.contrib import admin
from .models import Book
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')

    list_filter = ('author', 'published_date')

    search_fields = ('title', 'author')

class CustomUserAdmin(UserAdmin):
    model = CustomUser

admin.site.register(Book)
admin.site.register(CustomUser, CustomUserAdmin)