from django.urls import path

from .views import (
    index,
)

# namespace your urls, incase a different app uses 'new-post-page
app_name = "project"

urlpatterns = [
    path("", index, name="home"),
]
