from django.urls import path, include

from .views import index, post_page

urlpatterns = [
    path("", index),
    path("post/<int:id>", post_page)
]