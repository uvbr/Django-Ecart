# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Users


# Create your views here.

def register(request):


	if request.method=='GET':
		return render(request,'Register.html')
	else:
		uname = request.POST.get('uname')
		uemail = request.POST.get('uemail')
		upswd = request.POST.get('upswd')
		check_user =Users.objects.filter(username=uname,email=uemail)
		if check_user is None:
			user = Users.objects.create(username=uname,email=uemail,password=upswd)
			print user
			return HttpResponse('Successfully registered'+user.username)
		else:
			return HttpResponse('user already exists')

def login(request):

	if request.method == 'GET':

		uname = request.POST.get('uname')
		upswd = request.POST.get('upswd')


