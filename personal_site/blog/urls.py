from django.urls import path, include

from .views import index, post_page, new_post_page

urlpatterns = [
    path("", index, name="blog-home"),
    path("post", new_post_page, name="new-post-page"),
    path("post/<int:id>", post_page, name="post-page"),
]
