from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Author, PostForm

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
    form = PostForm()
    if request.method == 'POST':
        post = Post()
        author = Author.objects.get(id=request.POST['author'])
        post.post_body = request.POST['post_body']
        post.post_title = request.POST['post_title']
        post.author = author
        post.save()
        print(request.POST)
    return render(request, "blog/new_post.html", {'form': form})