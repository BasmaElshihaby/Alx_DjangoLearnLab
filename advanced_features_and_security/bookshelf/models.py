from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()
