from django.shortcuts import render
from .models import Post, PostForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Render does 3 in 1 - loads template, fills context, and retuns an
# HTTPResponse. You NEED to retun an HTTPResponse for each Django view.
from django.shortcuts import render
from django.http import JsonResponse
import os

# Create your views here.


def index(request):
    content = Post.objects.all()[5:]
    is_authenticated = request.user.is_authenticated
    return render(
        request,
        "blog/index.html",
        context={"content": content, "is_authenticated": is_authenticated},
    )


def chatgpt_page(request):
    return render(request, "blog/chatgpt.html")


def chatgpt_post(request):
    return render(request, "blog/chatgpt_post.html")


def post_page(request, id):
    post = Post.objects.get(id=id)
    is_authenticated = request.user.is_authenticated
    return render(
        request,
        "blog/post.html",
        {"post": post, "is_authenticated": is_authenticated, "post_id": id},
    )


@login_required
def create_post(request):
    if request.method == "GET":
        form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Nope, not valid")
        print(request.POST)
    return render(request, "blog/create_post.html", {"form": form})


@login_required
def edit_post(request, id):
    post_obj = Post.objects.get(pk=id)
    if request.method == "GET":
        form = PostForm(instance=post_obj)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post_obj)
        if form.is_valid():
            form.save()
    return render(request, "blog/edit_post.html", {"form": form, "post_id": id})


@csrf_exempt
def upload_image(request):
    print(request.FILES)
    file_obj = request.FILES["file"]
    dirname = os.path.dirname(__file__)
    print(f"The directory name {dirname}")
    relpath = os.path.join("static/blog/images", file_obj.name)
    print(f"The relative path name {relpath}")
    file_path = os.path.join(dirname, relpath)
    print(file_path)
    with open(file_path, "wb+") as f:
        for chunk in file_obj.chunks():
            f.write(chunk)
    return JsonResponse(
        {"message": "Image uploaded successfully", "location": "/" + relpath}
    )
