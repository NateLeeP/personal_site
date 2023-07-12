from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def post_page(request, id):
    content = Posts.objects.get(id=id)

    return HttpResponse(f"You're looking at post {id} with content {content.post} written by {content.author.name}")