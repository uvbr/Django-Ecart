# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Users,Products


# Create your views here.

def register(request):
    print 'a'
    if request.method=='GET':
        return render(request,'Register.html')
    else:
        uname = request.POST.get('uname')
        uemail = request.POST.get('uemail')
        upswd = request.POST.get('upswd')
        check_user = Users.objects.filter(username=uname,email=uemail)
        print len(check_user)
        if len(check_user) == 0:
            user = Users.objects.create(username=uname,email=uemail,password=upswd)
            context={'status':'successfully registered'}
            return render(request,'Login.html',context)
        else:
            return HttpResponse('user already exists')

def login(request):
    print 'b'

    if request.method == 'GET':
        if (Users.objects.filter(username=request.GET.get('uname'), password=request.GET.get('upswd'))).exists():
            member = Users.objects.get(username=request.GET.get('uname'), password=request.GET.get('upswd'))
            context={'items':Products.objects.all(),'member':member}
            print member
            return render(request,'home.html',context)
        return render(request,'Login.html')
    return render(request,'Login.html')

def home(request):
    print 'c'

    if request.GET.get('action') =='addtocart':
        id=request.GET.get('id')
        product = Products.objects.get(id=id)   
        if product.quant>product.num:
            product.num=product.num+1
        product.save()

    # if user buys item,then available num is decreased and cart will be zero
    if request.GET.get('action') =='buy':
        id=request.GET.get('id')
        product =Products.objects.get(id=id)
        if product.quant>product.num:
            product.quant=product.quant-product.num
            product.num=0
        product.save()

    # if user removes then the product in the cart will be removed 
    if request.GET.get('action') == 'remove':
        id=request.GET.get('id')
        product=Products.objects.get(id=id)
        if product.num>0:
            product.quant=product.quant+product.num
            product.num=0
            product.save()
    context={
            'item':Products.objects.all()
            } 
    return render(request,'home.html', context)

def adminlogin(request):
    print 'd'

    if request.method =='GET':
        # it checks whether username and password equals to admin
        if 'admin'== request.GET.get('uname') and 'admin' == request.GET.get('upswd') :
            context={   'items':Products.objects.all()  }
            # it prints each and every object in the database
            return render(request,'Adminhome.html',context)
        else:
            return render(request, 'Adminlogin.html')
    else:
        return redirect('/ecart/index')


def Adminhome(request):
    print 'e'
    table={ 'items':Products.objects.all() }
    
    if request.method == 'GET':     
        # checks whether category exists or not
        if Category.objects.filter(name=request.POST.get('cname')).exists():
            cate=Category.objects.get(name=request.POST.get('cname'))
        # if category doesnot exists,it creates category
        else:
            Category.objects.create(name=request.POST.get('cname'))
            cate=Category.objects.get(name=request.POST.get('cname'))
            #creates products in the respective category 
            item=Products.objects.create(category=cate,name=request.POST.get('pname'),
                quant=request.POST.get('pquant'),price=request.POST.get('pprice'))
            table={
                'items':Products.objects.all()
                }
    
    # if admin click on remove it removes the product from the data base
    if request.GET.get('action') =='remove':
        id = request.GET.get('id')
        record = Products.objects.get(id=id)
        record.delete()
        table={ 'items':Products.objects.all() }

    return render(request,'Adminhome.html',table)

