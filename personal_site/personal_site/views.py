from django.http import HttpResponse
from django.template import loader


def home(request):
    home_template = loader.get_template("base_templates/index.html")
    return HttpResponse(home_template.render({}, request))
