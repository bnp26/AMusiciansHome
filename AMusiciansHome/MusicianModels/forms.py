from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User as Musician

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(min_length=4, max_length=18, required=True, help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email1 = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    email2 = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', widget=forms.EmailInput(attrs={'placeholder': 'Confirm Email'}))
    phone_num = forms.CharField(max_length=12, required=False, help_text='phone number', widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    password1 = forms.CharField(min_length=6, max_length=18, required=True, help_text='password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(min_length=6, max_length=18, required=True, help_text='confirm password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    
    def save(self):
        data = self.cleaned_data
        
        if data['email1'] != data['email2']:
            return None
        else:
            email = data['email1']
        
        if data['password1'] != data['password2']:
            return None
        else:
            password = data['password1']
        
        user = User.objects.create(username=data['username'],
                                   email = email,
                                   password = password,)
        
        user.save()
        
        musician = Musician.objects.create(user=user,
                                          first_name=data['first_name'],
                                          last_name=data['last_name'],
                                          phone_num=data['phone_num'],)
        
        musician.save()