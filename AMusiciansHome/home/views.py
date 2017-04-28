from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext, Context, loader
from django.core.urlresolvers import reverse
import pdb

from MusicianModels.forms import RegistrationForm, LoginForm, User, ProfileForm, InstrForm
from MusicianModels.models import Musician, Object, Tag, Instr, Supply, Music

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
        registration_form = RegistrationForm(request.POST)
        #user['phone_num'] = '2162223333'
        if registration_form.is_valid():
            #need to send email
            cleaned_data = registration_form.clean()
            registration_form.save(cleaned_data)
            template = 'home/home.html'
            context = {}
            return redirect('/')
    else:
        template = 'home/register.html'
        musicianForm = RegistrationForm ()
        context = {'form': musicianForm}
        return render(request, template, context)

def main_page(request):
    form = InstrForm()
    tags = Tag.objects.order_by('tag_type')
    context = {'form':form, 'tags':tags}
    for tag in tags:
        print tag.tag_type
    template = 'home/main.html'
    return render(request, template, context)

@login_required
def user_lib_page(request):
    context = {}
    template = 'home/my_library.html'
    return render(request, template, context)
  
@login_required
def profile_page(request):
    if request.method == 'POST':
        musician = Musician.objects.get(user=request.user)
        user = request.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.username = request.POST['username']
        user.save()
        musician.phone_num = request.POST['phone_num']
        musician.save()
        return redirect('/profile')
    else:
        musician = Musician.objects.get(user=request.user)
        data = {'first_name':musician.user.first_name,
                'last_name':musician.user.last_name,
                'email':musician.user.email,
                'username':musician.user.username,
                'phone_num':musician.phone_num}
        form = ProfileForm(data, initial=data)
        context = {'form':form}
        template = 'home/profile.html'
        return render(request, template, context)

@login_required
def logout_request(request):
    logout(request)
    return redirect('/')