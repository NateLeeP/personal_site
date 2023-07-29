from django.db import models
from datetime import datetime
from django.forms import ModelForm
from tinymce.widgets import TinyMCE

# Create your models here.


class Author(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=20)


class Post(models.Model):
    def __str__(self):
        return self.post_title

    post_body = models.TextField()
    post_title = models.CharField(max_length=20, unique=True)
    published_at = models.DateField(null=True, blank=True)
    updated_at = models.DateField(auto_now_add=True)
    # Author name for now - will be ID later. Notably, if I assign it as a 'foreign'
    # key, Django will handle the id automatically.
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class PostForm(ModelForm):
    class Meta:
        model= Post
        fields = ["post_body", "post_title", "author"]
        widgets = {
            "post_body": TinyMCE(attrs={'cols': 80, 'rows': 30})
        }
        labels = {
            'post_body': "Write your cool blog dude"
        }
        error_messages = {
            'post_title': {
                'unique': 'You need a unique message'
            }
        }