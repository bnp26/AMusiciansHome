from __future__ import unicode_literals
import django
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Musician(models.Model):
    user = models.OneToOneField(User)
    phone_num = models.CharField(max_length=10, blank=False)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.user.username
    
    @classmethod
    def create(cls, c_first_name, c_last_name, c_phone_num, c_email, c_username, c_password):
        c_user = User.objects.create_user(first_name=c_first_name, last_name=c_last_name, email=c_email, username=c_username, password=c_password)
        musician = cls(phone_num=c_phone_num, user=c_user)
        
        return musician

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    tag_type = models.CharField(max_length=15)

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Object(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    est_price = models.IntegerField()
    date_posted = models.DateTimeField(default=django.utils.timezone.now(), blank=True)
    post = models.BooleanField()
    tags = models.ManyToManyField(Tag, blank=True)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name
    
class Instr(models.Model):
    obj = models.ForeignKey(Object, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    maker = models.CharField(max_length=30)
    year_made = models.IntegerField(blank=False)

class Supply(models.Model):
    obj = models.ForeignKey(Object, on_delete=models.CASCADE)
    maker = models.CharField(max_length=30, blank=False)
    year_made = models.IntegerField(blank=True)
    description = models.CharField(max_length=120)

class Music(models.Model):
    obj = models.ForeignKey(Object, on_delete=models.CASCADE)
    num_pages = models.IntegerField()
    title = models.CharField(max_length=30)
    composer = models.CharField(max_length=30)
    date_pub = models.DateField()

