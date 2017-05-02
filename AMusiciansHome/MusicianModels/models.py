from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
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
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    tag_type = models.CharField(max_length=15)

    def __str__(self):              # __unicode__ on Python 2
        return self.name
    
    class Meta:
        ordering = ('name',)

class Object(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    est_price = models.IntegerField()
    date_posted = models.DateField(auto_now=True)
    post = models.BooleanField()
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name
    
    class Meta:
        ordering = ('name',)
    
#     @classmethod
#     def create(cls, c_name, c_user, c_est_price, c_post, c_tags):
#         time = timezone.now()
#         obj = cls(name=c_name, user=c_user, est_price=c_est_price, post=c_post, tags=c_tags, date_posted=time)
#         return obj

class Instr(models.Model):
    obj = models.ForeignKey(Object, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    maker = models.CharField(max_length=30)
    year_made = models.IntegerField(blank=False)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.obj.name

class Supply(models.Model):
    obj = models.ForeignKey(Object, on_delete=models.CASCADE)
    maker = models.CharField(max_length=30, blank=False)
    year_made = models.IntegerField(blank=True)
    description = models.CharField(max_length=120)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.obj.name

class Music(models.Model):
    obj = models.ForeignKey(Object, on_delete=models.CASCADE)
    num_pages = models.IntegerField()
    title = models.CharField(max_length=30)
    composer = models.CharField(max_length=30)
    year_pub = models.IntegerField(blank=True, default=1905)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.obj.name

