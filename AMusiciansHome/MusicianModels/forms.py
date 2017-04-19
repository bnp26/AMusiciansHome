from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User as Musician

class LoginForm(forms.Form):
    username = forms.CharField(max_length=18, required=True, help_text='username', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=18, required=True, help_text='password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(min_length=4, max_length=18, required=True, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    phone_num = forms.CharField(max_length=12, required=True, help_text='phone number', widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    password1 = forms.CharField(min_length=6, max_length=18, required=True, help_text='password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(min_length=6, max_length=18, required=True, help_text='confirm password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    
    def save(self):
        data = self.cleaned_data
        
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