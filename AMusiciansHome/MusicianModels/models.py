from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Musician(models.Model):
    user = models.OneToOneField(User)
    phone_num = models.CharField(max_length=10, blank=False)
    
    @classmethod
    def create(cls, c_first_name, c_last_name, c_phone_num, c_email, c_username, c_password):
        c_user = User.objects.create_user(first_name=c_first_name, last_name=c_last_name, email=c_email, username=c_username, password=c_password)
        musician = cls(phone_num=c_phone_num, user=c_user)
        
        return musician

class Object(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    est_price = models.IntegerField()
    date_posted = models.DateField()

class Tag(models.Model):
    name = models.CharField(max_length=30)
    tag_type = models.CharField(max_length=15)
    objects = models.ManyToManyField(Object)

class Instr(models.Model):
    obj = models.ForeignKey(Object, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    maker = models.CharField(max_length=30)
    date_made = models.DateField()

class Supply(models.Model):
    obj = models.ForeignKey(Object, on_delete=models.CASCADE)
    maker = models.CharField(max_length=30)
    date_made = models.DateField()
    description = models.CharField(max_length=120)

class Music(models.Model):
    obj = models.ForeignKey(Object, on_delete=models.CASCADE)
    num_pages = models.IntegerField()
    title = models.CharField(max_length=30)
    composer = models.CharField(max_length=30)
    date_pub = models.DateField()

