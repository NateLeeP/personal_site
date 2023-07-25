from django.urls import path, include

from .views import index, post_page, new_post_page

# namespace your urls, incase a different app uses 'new-post-page
app_name = 'blog'

urlpatterns = [
    path("", index, name="home"),
    path("post", new_post_page, name="new-post-page"),
    path("post/<int:id>", post_page, name="post-page"),
]
