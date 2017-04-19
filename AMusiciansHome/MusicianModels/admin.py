from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Musician)
admin.site.register(Object)
admin.site.register(Tag)
admin.site.register(Instr)
admin.site.register(Supply)
admin.site.register(Music)