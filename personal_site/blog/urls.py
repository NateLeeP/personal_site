from django.urls import path

from .views import index, post_page, create_post, edit_post

# namespace your urls, incase a different app uses 'new-post-page
app_name = 'blog'

urlpatterns = [
    path("", index, name="home"),
    path("create_post", create_post, name="create-post"),
    path("post/<int:id>", post_page, name="post-page"),
    path("edit_post/<int:id>", edit_post, name="edit-post")
]
