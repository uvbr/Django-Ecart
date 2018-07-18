from django.conf.urls import url,include

from . import views

urlpatterns = [
    url('index', views.index, name='index'),
]
