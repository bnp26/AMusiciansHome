from __future__ import unicode_literals


from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    username = models.CharField(max_length=10)
    phone_num = models.CharField(max_length=10)

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
    obj = models.ForeignKey(Object, on_delete_models.CASCADE)
    size = models.CharField(max_length=10)
    maker = models.CharField(max_length=30)
    date_made = models.DateField()

class Supply(models.Model):
    obj = models.ForeignKey(Object, on_delete_models.CASCADE)
    maker = models.CharField(max_length=30)
    date_made = models.DateField()
    description = models.CharField(max_length=120)

class Music(models.Model):
    obj = models.ForeignKey(Object, on_delete_models.CASCADE)
    num_pages = models.IntegerField()
    title = models.CharField(max_length=30)
    composer = models.CharField(max_length=30)
    date_pub = models.Date()

