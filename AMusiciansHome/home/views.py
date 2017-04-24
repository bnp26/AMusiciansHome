from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext, Context, loader
from django.core.urlresolvers import reverse

from MusicianModels.forms import RegistrationForm, LoginForm, User

#View for the homepage
def homepage(request):
    
    context = {}
    if request.user.is_authenticated():
        context['username'] = request.user
    template = 'home/home.html'
    return render(request, template, context)

#just a plce holder to edit the login page
def login_page(request):
    request_context = RequestContext(request)
    context = {}    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('/')
        else:
            context = {'login': 'failed'}
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        template = 'home/login.html'
        form = LoginForm()
        context = {'form': form}
        return render(request, template, context)

#place holder for sign up page
def register_page(request):
    request_context = RequestContext(request)
    context = Context()
    if request.method == 'POST':
        form = RegistrationForm(request.POST) 
        if form.is_valid():
            #need to send email
            template = 'home/home.html'
            context = {}
            return redirect('/')
    else:
        template = 'home/register.html'
        form = RegistrationForm ()
        context = {'form': form}
        return render(request, template, context)

def main_page(request):
    context = {}
    template = 'home/main.html'
    return render(request, template, context)

def user_lib_page(request):
    context = {}
    template = 'home/my_library.html'
    return render(request, template, context)
  
def profile_page(request):
  context = {}
  template = 'home/profile.html'
  return render(request, template, context)

@login_required
def logout_request(request):
    logout(request)
    return redirect('/')