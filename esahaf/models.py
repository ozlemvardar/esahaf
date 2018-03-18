from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Author(models.Model):
    name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    bio = models.TextField(null=True)


class Book(models.Model):
    title = models.TextField()
    isbn = models.CharField(null=True, max_length=100)
    author = models.ForeignKey(Author)
    user = models.ManyToManyField(User)


class Profile(models.Model):
    user = models.OneToOneField(User)
    phone_number = models.CharField(max_length=15, null=True)


