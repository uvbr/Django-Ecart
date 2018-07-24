from django.conf.urls import url,include

from . import views

urlpatterns = [
    url('register', views.register),
    url('login', views.login),
    url('home', views.home),
    url('adminauth', views.adminauth),
    url('Adminindex', views.Adminindex),

]
