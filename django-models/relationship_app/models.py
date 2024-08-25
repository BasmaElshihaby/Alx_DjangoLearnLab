from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.AutoField(primary_key=True)

class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=64, choices=[('Admin', 'Admin'), ('Librarian', 'Librarian'), ('Member', 'Member')])

# Create your models here.
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name 
    
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

class Library(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    books = models.ManyToManyField(Book, related_name='libraries')

class Librarian(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)