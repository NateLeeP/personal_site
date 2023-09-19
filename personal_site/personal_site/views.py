from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def home(request):
    home_template = loader.get_template("base_templates/index.html")
    return HttpResponse(home_template.render({}, request))


def about_me(request):
    return render(request, "base_templates/about_me.html")
