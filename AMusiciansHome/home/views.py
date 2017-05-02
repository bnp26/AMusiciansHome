from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.template import RequestContext, Context, loader
from django.core.urlresolvers import reverse
import pdb

from MusicianModels.forms import RegistrationForm, LoginForm, User, ProfileForm, InstrForm, SupplyForm, MusicForm
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
    if request.is_ajax():
        username = request.GET.get('username', None)
        email = request.GET.get('email', None)
        phone_number = request.GET.get('phone_num', None)
        data = {
            'username_is_taken': User.objects.filter(username__iexact=username).exists(),
            'email_is_taken': User.objects.filter(email__iexact=email).exists(),
            'phone_num_is_taken': Musician.objects.filter(phone_num__iexact=phone_number).exists()
        }
        return JsonResponse(data)
    elif request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        #user['phone_num'] = '2162223333'
        if registration_form.is_valid():
            #need to send email
            cleaned_data = registration_form.clean()
            registration_form.save(cleaned_data)
            context = {}
            return redirect('/')
    else:
        template = 'home/register.html'
        musicianForm = RegistrationForm ()
        context = {'form': musicianForm}
        return render(request, template, context)

def main_page(request):
    if request.is_ajax():
        instrs = []
        supplies = []
        music = []
        try:
            tagged = request.GET['selected_tags']
            if tagged == "":
                instrs = list(Instr.objects.filter(obj__post=True))
                supplies = list(Supply.objects.filter(obj__post=True))
                music = list(Music.objects.filter(obj__post=True))
            else:
                tags_str = tagged.split(',')
                for string in tags_str:
                    if string == "":
                        break
                    instrs = list(Instr.objects.filter(obj__post=True, obj__tags=Tag.objects.filter(name=string)))
                    supplies = list(Supply.objects.filter(obj__post=True, obj__tags=Tag.objects.filter(name=string)))
                    music = list(Music.objects.filter(obj__post=True, obj__tags=Tag.objects.filter(name=string)))
        except:
            instrs = list(Instr.objects.filter(obj__post=True))
            supplies = list(Supply.objects.filter(obj__post=True))
            music = list(Music.objects.filter(obj__post=True))
            
        print instrs
        print supplies
        print music
        context = {"instruments":instrs, "supplies":supplies, "music":music}
        template = 'home/browser_body.html'

        return render(request, template, context)
    
    instruments = Instr.objects.filter(obj__post=True)
    supplies = Supply.objects.filter(obj__post=True)
    object_num = Object.objects.all().distinct().values('user_id').annotate(user_count=Count('user_id')).filter(user_count__gt=1).order_by('user_id').count()
    for_all_query = Object.objects.all().distinct().values('user_id').annotate(user_count=Count('user_id')).filter(user_count__gt=5).order_by('user_id')
    istr_objs = Object.objects.all().filter().values('user_id').annotate(user_count=Count('user_id')).filter(user_count__gt=5).order_by('user_id')
    #flute_query = Object.objects.raw('SELECT U.username FROM auth_user U, MusicianModels_object O1, MusicianModels_tag T1, MusicianModels_object_tags OT1 WHERE U.id = O.user_id AND O.id = OT1.object_id AND OT1.tag_id = T1.tag_id AND T1.name = "Flute" AND NOT EXISTS (SELECT U.username FROM auth_user U, MusicianModels_tag T, MusicianModels_object O, MusicianModels_object_tags OT WHERE U.id = O.user_id AND O.id =  OT.object_id AND T.id = OT.tag_id AND T.name != "Flute")')
    users_for_all = []
    for user in for_all_query:
        users_for_all.append(User.objects.get(id=user['user_id']))
    
    music = Music.objects.filter(obj__post=True)
    print instruments
   
    tags = Tag.objects.order_by('tag_type')
    context = {'tags':tags, 'instruments':instruments, 'supplies':supplies, 'music':music, 'num_objs':object_num, 'for_all':users_for_all}
    template = 'home/main.html'
    return render(request, template, context)

@login_required
def user_lib_page(request):
    if request.method == 'POST':
        if 'instrument' in request.POST:
            instr_form = InstrForm(request.POST)
            print instr_form.errors
            print instr_form.is_valid()
            if instr_form.is_valid():
                cleaned_data = instr_form.clean()
                cleaned_data['user'] = request.user
                instr_form.save(cleaned_data)
                return redirect('/library')
            else:
                return redirect('/library')
        elif 'supply' in request.POST:
            supply_form = SupplyForm(request.POST)
            if supply_form.is_valid():
                supply_data = {'maker':request.POST['maker'],
                       'year_made':request.POST['year_made'],
                       'description':request.POST['description'],
                       'name':request.POST['name']}
                supply_data.append(obj_data)
                cleaned_data = supply_form.clean()
                supply_form.save(cleaned_data)
                return redirect('/library')
        elif 'music' in request.POST:
            music_form = MusicForm(request.POST)
            if music_form.is_valid():
                music_data = {'title':request.POST['title'],
                     'composer':request.POST['composer'],
                     'num_pages':request.POST['num_pages'],
                     'year_pub':request.POST['year_pub']}
                music_data.append(obj_data)
                cleaned_data = music_form.clean()
                music_form.save(cleaned_data)
                return redirect('/library')
        else:
            return redirect('/library')    
    else:
        tags = Tag.objects.all()
        supply_form = SupplyForm()
        music_form = MusicForm()
        instr_form = InstrForm()
        userId = request.user.id
        
        instrs = Instr.objects.filter(obj__user_id=userId)
        supplies = list(Supply.objects.filter(obj__user_id=userId))
        music = list(Music.objects.filter(obj__user_id=userId))
        
        obj_count = Object.objects.filter(user_id=userId).count()
        context = {'instr_form':instr_form, 'supply_form':supply_form, 'music_form':music_form, 'tags':tags, 'instruments':instrs, 'supplies':supplies, 'music':music, 'obj_count':obj_count}
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