from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from quickstart.models import User
from quickstart.models import Task
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    name = request.POST['username']
    password = request.POST['password']

    user = User.objects.all().filter(username=name, password=password)
    if user:
        response = HttpResponseRedirect(reverse('home'))
        response.set_cookie('username', name, 3600)
        return response
    else:
        return HttpResponseRedirect(reverse('index'))


def logout(request):
    response = HttpResponseRedirect(reverse('index'))
    response.delete_cookie('username')

    return response

def home(request):
    username = request.COOKIES.get('username', '')
    tasks = Task.objects.all().filter(username=username)
    return render_to_response('home.html', {'username': username, 'tasks': tasks}, context_instance=RequestContext(request))

def addtask(request):
    taskinfo = request.POST['taskinfo']
    name = request.COOKIES.get('username')

    task = Task(username=name, taskinfo=taskinfo)
    task.save()

    # return
    return HttpResponse(json.dumps({"code": 1, "message": {"taskinfo": taskinfo}}))

def deltask(request):
    taskinfo = request.POST['taskinfo']
    name = request.COOKIES.get('username')

    Task.objects.filter(taskinfo=taskinfo, username=name).delete()

    # return
    return HttpResponse(json.dumps({"code": 1, "message": {"taskinfo": taskinfo}}))