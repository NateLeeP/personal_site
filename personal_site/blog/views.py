from django.shortcuts import render
from .models import Post, PostForm
from django.contrib.auth.decorators import login_required
# Render does 3 in 1 - loads template, fills context, and retuns an
# HTTPResponse. You NEED to retun an HTTPResponse for each Django view.
from django.shortcuts import render

# Create your views here.


def index(request):
    content = Post.objects.all()
    is_authenticated = request.user.is_authenticated
    return render(request, "blog/index.html", context={"content": content, "is_authenticated": is_authenticated})


def post_page(request, id):
    post = Post.objects.get(id=id)
    is_authenticated = request.user.is_authenticated
    return render(request, "blog/post.html", {"post": post, "is_authenticated": is_authenticated, 'post_id': id})

@login_required
def create_post(request):
    if request.method == "GET":
        form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('Nope, not valid')
        print(request.POST)
    return render(request, "blog/create_post.html", {'form': form})

@login_required
def edit_post(request, id):
    post_obj = Post.objects.get(pk=id)
    if request.method == "GET":
        form = PostForm(instance=post_obj)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post_obj)
        if form.is_valid():
            form.save()
    return render(request, "blog/edit_post.html", {'form': form, 'post_id': id})