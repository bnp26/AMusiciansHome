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
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class':'validate'}))
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
        pdb.set_trace()
        musician = Musician.create(data.get('first_name'), data.get('last_name'), data.get('phone_num'), data.get('email'), data.get('username'), data.get('password1'))
        musician.user.save()
        musician.save()

class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class':'validate'}))
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class':'validate'}))
    username = forms.CharField(min_length=4, max_length=18, required=True, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'Username', 'class':'validate'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class':'validate'}))
    phone_num = forms.CharField(max_length=12, required=True, help_text='phone number', widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'class':'validate'}))

class InstrForm(forms.Form):
    name = forms.CharField(max_length=30, required=True, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class':'validate'}))
    est_price = forms.IntegerField()
    date_posted = forms.DateField()
    post = forms.BooleanField()
    size = forms.CharField(max_length=10)
    maker = forms.CharField(max_length=30)
    date_made = forms.DateField()
    tags = AutoCompleteSelectMultipleField('tags', required=False, help_text=None)

    def save(self, data):
        obj = Object(user=data.get('user'), name=data.get('name'), est_price=data.get('est_price'), post=data.get('post'))
        obj.save()
        instr = Instr(obj=obj, size=data.get('size'), maker=data.get('maker'), date_made=data.get('date_made'))
        tags = data.get('tags')
        for tag in tags:
            instr.tags.add(tag)
        instr.save()
        
        

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