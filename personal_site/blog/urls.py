from django.urls import path, include

from .views import index, post_page

url_paths = [
    path("", index),
    path("post/<int:id>", post_page)
]