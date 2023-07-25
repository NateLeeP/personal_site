from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Render does 3 in 1 - loads template, fills context, and retuns an
# HTTPResponse. You NEED to retun an HTTPResponse for each Django view.
from django.shortcuts import render

# Create your views here.


def index(request):
    content = Post.objects.all()
    return render(request, "blog/index.html", context={"content": content})


def post_page(request, id):
    post = Post.objects.get(id=id)

    return render(request, "blog/post.html", {"post": post})


def new_post_page(request):
    print(request)
    
    if request.method == 'POST':
        print(request.POST)
        print(request.POST['blog-body'])
    return render(request, "blog/new_post.html")