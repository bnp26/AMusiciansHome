from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

#View for the homepage
def homepage(request):
    template = 'home/home.html'
    context = {}
    return render(request, template, context)
