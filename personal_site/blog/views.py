from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def post_page(request, id):
    return HttpResponse(f"You're looking at post {id}")