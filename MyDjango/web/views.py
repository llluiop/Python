from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
from models import Person

def current_time(request):
    now = datetime.datetime.now()

    html = "<html><body>It is now %s.</body></html>" % now

    return HttpResponse(html)


def add(request, a, b):
    c = int(a) + int(b)

    return HttpResponse(c)


def home(request):
    return render(request, 'index.html')

def person(request):
    name = 'person in table are:'
    for p in Person.objects.all():
        name += p.name

    return HttpResponse(name)

