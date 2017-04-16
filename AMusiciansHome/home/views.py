from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

#View for the homepage
def homepage(request):
    template = 'home/home.html'
    context = {}
    return render(request, template, context)

#just a plce holder to edit the login page
def login_page(request):
    template = 'home/login.html'
    context = {}
    return render(request, template, context)

#place holder for sign up page
def register_page(request):
    template = 'home/register.html'
    context = {}
    return render(request, template, context)