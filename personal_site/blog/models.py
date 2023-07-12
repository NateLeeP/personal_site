from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)

class Posts(models.Model):
    post = models.TextField()
    # Author name for now - will be ID later. Notably, if I assign it as a 'foreign'
    # key, Django will handle the id automatically. 
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

