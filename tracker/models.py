from django.db import models
from django.utils import timezone

class Purchase(models.Model):
    type = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    time = models.DateTimeField(default=timezone.now)
    seller = models.CharField(max_length=10)

class Bookmark(models.Model):
    ''' create bookmark'''
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
