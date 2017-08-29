# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Customer(models.Model):
    GENDER_CHOICES = (('M', "Male"), ('F', "Female"), ('O', "Other"))
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length =100)
    middle_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=13, null=False)
    alternate_number = models.CharField(max_length=13, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    created_date = models.DateTimeField(null=False)
    modified_date = models.DateTimeField(null=False)

