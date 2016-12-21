from __future__ import unicode_literals

from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=225,null=True, blank=True)
    Amount = models.FloatField()
    phone = models.CharField(max_length=10)
    date = models.DateField()