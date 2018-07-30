"""urls.py contains the urls and the corresponding views
which has to be called.
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url('register', views.register),
    url('login', views.login),
    url('home', views.home),
    url('adminauth', views.adminauth),
    url('Adminindex', views.Adminindex),

]
