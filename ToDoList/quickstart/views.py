from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from quickstart.models import User
from quickstart.models import Task

# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(label='username:', max_length=100)
    password = forms.CharField(label='password:', widget=forms.PasswordInput())
    email = forms.EmailField(label='email:')

# Create your views here.
def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():

            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            email = uf.cleaned_data['email']

            user = User()
            user.username = username
            user.password = password
            user.email = email
            user.save()

            return render_to_response('success.html', {'username':username})
    else:
        uf = UserForm()
    return render_to_response('register.html', {'uf': uf}, context_instance=RequestContext(request))


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
        return HttpResponseRedirect(reverse('index/'))


def logout(request):
    response = HttpResponseRedirect(reverse('index'))
    response.delete_cookie('username')

    return response

def home(request):
    username = request.COOKIES.get('username', '')
    tasks = Task.objects.all()
    return render_to_response('home.html', {'username': username, 'tasks': tasks})

