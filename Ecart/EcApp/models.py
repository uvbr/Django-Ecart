# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.

class Users(models.Model):

	username = models.CharField(max_length=20)
	email = models.CharField(max_length=20)
	password = models.CharField(max_length=20)

	def __str__(self):
		return self.username

class Category(models.Model):
    name = models.CharField(max_length=255) 
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.name
        

class Products(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=255)
    quant=models.IntegerField()
    num=models.IntegerField(default=0)
    price=models.DecimalField(max_length=255, decimal_places=2, max_digits=10)
    date = models.DateField(default=datetime.now)
    
    def __str__(self):
        return self.name 

