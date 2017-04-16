from django.conf.urls import url

from . import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.homepage, name='index'),
    url(r'^login', views.login_page, name='login'),
    url(r'^register', views.register_page, name='register'),
]
