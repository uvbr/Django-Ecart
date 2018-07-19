from django.conf.urls import url,include

from . import views

urlpatterns = [
    url('register', views.register),
    url('login', views.login),

]
