from ajax_select import make_ajax_field
from ajax_select.fields import AutoCompleteSelectMultipleField

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
import pdb
from .models import Musician, Object, Instr, Supply, Music, Tag

class LoginForm(forms.Form):
    username = forms.CharField(max_length=18, required=True, help_text='username', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=18, required=True, help_text='password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
        
class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.', widget=forms.TextInput(attrs={'place`holder': 'First Name', 'class':'validate'}))
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class':'validate'}))
    username = forms.CharField(min_length=4, max_length=18, required=True, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'Username', 'class':'validate'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class':'validate'}))
    phone_num = forms.CharField(max_length=12, required=True, help_text='phone number', widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'class':'validate'}))
    password1 = forms.CharField(min_length=6, max_length=18, required=True, help_text='password', widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class':'validate'}))
    password2 = forms.CharField(min_length=6, max_length=18, required=True, help_text='confirm password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password' , 'class':'validate'}))
    
    def clean(self):
        data = super(RegistrationForm, self).clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")

        return self.cleaned_data

    def save(self):
        musician = Musician.create(self.cleaned_data.get('first_name'), self.cleaned_data.get('last_name'), self.cleaned_data.get('phone_num'), self.cleaned_data.get('email'), self.cleaned_data.get('username'), self.cleaned_data.get('password1'))
        musician.save()
    
    def save(self, data):
        musician = Musician.create(data.get('first_name'), data.get('last_name'), data.get('phone_num'), data.get('email'), data.get('username'), data.get('password1'))
        musician.user.save()
        musician.save()

class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class':'validate'}))
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class':'validate'}))
    username = forms.CharField(min_length=4, max_length=18, required=True, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'Username', 'class':'validate'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class':'validate'}))
    phone_num = forms.CharField(max_length=12, required=True, help_text='phone number', widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'class':'validate'}))

class InstrForm(ModelForm):
    name = forms.CharField(max_length=30, required=True, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'Instrument Name', 'class':'validate'}))
    est_price = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder':0, 'class':'validate'}))
    #date_posted = forms.DateField()
    post = forms.BooleanField(required=True, widget=forms.CheckboxInput())
    tags = forms.ChoiceField(widget=forms.Select(attrs={'multiple':'', 'placeholder':'Add Tags'}), required=False)
    
    class Meta:
        model = Instr
        fields = ['size', 'maker', 'year_made']
     
    def save(self, data):
        user = data.get('user')
        print user
        new_user = User.objects.get(username=user.get_username())
        tag = [Tag.objects.get(id=int(data.get('tags'))),]
        obj = Object(user=new_user, name=data.get('name'), est_price=data.get('est_price'), post=data.get('post'))
        obj.save()
        obj.tags = tag
        obj.save()
        instr = Instr(obj=obj, size=data.get('size'), maker=data.get('maker'), year_made=data.get('year_made'))
        instr.save()
        
    def __init__(self, *args, **kwargs):
        super(InstrForm, self).__init__(*args, **kwargs)
        self.fields['tags'].choices = [(x.pk, x.name) for x in Tag.objects.all()] 

class SupplyForm(ModelForm):
    #Object
    name = forms.CharField(max_length=30, required=True, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'Supply Name', 'class':'validate'}))
    est_price = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder':0, 'class':'validate'}))
#    date_posted = forms.DateField()
    post = forms.BooleanField(widget=forms.CheckboxInput(attrs={'type':'checkbox'}))
    tags = forms.MultipleChoiceField(widget=forms.Select(attrs={'name':'', 'multiple':'', 'placeholder':'Add Tags'}), required=False)
    
    class Meta:
        model = Supply
        fields = ['maker', 'year_made', 'description']
    
    
    def save(self, data):
        user = data.get('user')
        print user
        new_user = User.objects.get(username=user.get_username())
        tag = [Tag.objects.get(id=int(data.get('tags'))),]
        obj = Object(user=new_user, name=data.get('name'), est_price=data.get('est_price'), post=data.get('post'))
        obj.save()
        obj.tags = tag
        obj.save()
        supply = Supply(obj=obj, maker=data.get('maker'), year_made=data.get('year_made'), description=data.get('description'))
        supply.save()
    
    def __init__(self, *args, **kwargs):
        super(SupplyForm, self).__init__(*args, **kwargs)
        self.fields['tags'].choices = [(x.pk, x.name) for x in Tag.objects.all()] 
        
class MusicForm(ModelForm):
     #Object
    est_price = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder':0, 'class':'validate'}))
    #date_posted = forms.DateField()
    post = forms.BooleanField(required=True, widget=forms.CheckboxInput(attrs={'type':'checkbox'}))
    tags = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'name':'', 'multiple':'', 'placeholder':'Add Tags'}), required=False)
    
    class Meta:
        model = Music
        fields = ['title', 'composer', 'num_pages', 'year_pub']
    
    def save(self, data):
        user = data.get('user')
        new_user = User.objects.get(username=user.get_username())
        tag = [Tag.objects.get(id=int(data.get('tags'))),]
        obj = Object(user=new_user, name= data.get('title') + ' ' + data.get('composer'), est_price=data.get('est_price'), post=data.get('post'))
        obj.save()
        obj.tags = tag
        obj.save()
        music = Music(obj=obj, title=data.get('title'), composer=data.get('composer'), num_pages=data.get('num_pages'), date_pub=data.get('date_pub'))
        music.save()
    
    def __init__(self, *args, **kwargs):
        super(MusicForm, self).__init__(*args, **kwargs)
        self.fields['tags'].choices = [(x.pk, x.name) for x in Tag.objects.all()]

'''
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class':'validate'}))
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class':'validate'}))
    username = forms.CharField(min_length=4, max_length=18, required=True, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'Username', 'class':'validate'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class':'validate'}))
    phone_num = forms.CharField(max_length=12, required=True, help_text='phone number', widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'class':'validate'}))
    password1 = forms.CharField(min_length=6, max_length=18, required=True, help_text='password', widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class':'validate'}))
    password2 = forms.CharField(min_length=6, max_length=18, required=True, help_text='confirm password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password' , 'class':'validate'}))
    
    def save(self):
        data = data
        
        if data['password1'] != data['password2']:
            return None
        else:
            password = data['password1']
        
        user = User.objects.create(username=data['username'],
                                   email = data['email'],
                                   password = password,
                                   first_name=data['first_name'],
                                   last_name=data['last_name'],)
        
        user.save()
        
        musician = Musician.objects.create(user=user,
                                          phone_num=data['phone_num'],)
        
        musician.save()
'''