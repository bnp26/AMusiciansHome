from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext, Context
from MusicianModels.models import User
from MusicianModels.forms import RegistrationForm

#View for the homepage
def homepage(request):
    template = 'home/home.html'
    context = {}
    return render(request, template, context)

#just a plce holder to edit the login page
def login_page(request):
    request_context = RequestContext(request)
    context = Context()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        
        if user:
            template = 'home/home.html'
            context['login': 'success']
            print "successful login: {0}, {1}".format(username, password)
            return render(request, template, context)
        else:
            context = {'login': 'failed'}
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        template = 'home/login.html'
        context = {}
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
            return render(request, template, context)
    else:
        template = 'home/register.html'
        form = RegistrationForm()
        context = {'form': form}
        return render(request, template, context)