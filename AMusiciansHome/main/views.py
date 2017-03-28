from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class HomeView(View):
    
    def get(self, request):
        # <view logic>
        template_name = ''
        return render(request, request.template_name)

# Create your views here.
