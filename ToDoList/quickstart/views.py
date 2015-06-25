from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from quickstart.models import User

# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(label='username:',max_length=100)
    password = forms.CharField(label='password:',widget=forms.PasswordInput())
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

            return render_to_response('success.html',{'username':username})
    else:
        uf = UserForm()
    return render_to_response('register.html',{'uf':uf},context_instance=RequestContext(request))


def index(request):
    return render(request, 'index.html')

def login(request):
