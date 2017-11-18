# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 30)
    created_on = models.DateTimeField(auto_now_add= True)
