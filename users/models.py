# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField('auth.user', related_name = 'profile')
	phone = models.CharField(max_length = 15, default = True)
	gender = models.CharField(max_length = 15, default = True)
