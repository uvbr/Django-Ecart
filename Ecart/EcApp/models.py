"""models.py contains the blueprint of tables in the database.
"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.

class Users(models.Model):
    """Users model is mainly used to store user data i.e., for
    Register.
    """

    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Category(models.Model):
    """Category model is mainly used to parent level for products
    """

    name = models.CharField(max_length=255)
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.name


class Products(models.Model):
    """Products model is mainly used to store info products in the data
    base
    """

    category = models.ForeignKey(Category)
    name = models.CharField(max_length=255)
    quant = models.IntegerField()
    num = models.IntegerField(default=0)
    price = models.DecimalField(max_length=255, decimal_places=2, max_digits=10)
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.name
