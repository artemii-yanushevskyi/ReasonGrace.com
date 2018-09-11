from django.db import models
# from django.contrib.postgres.fields import JSONField
# Create your models here.

from django.db import models
from django.utils import timezone

# class Post(models.Model):
#     ''' create post class '''
#     author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField( default=timezone.now)
#     published_date = models.DateTimeField( blank=True, null=True)
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     def __str__(self):
#         return self.title

class Bookmark(models.Model):
    ''' create bookmark'''
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)


# class Moment(models.Model):
#     ''' create moment class'''
#     time = models.DateTimeField(default=timezone.now)
#     name = models.CharField(max_length=500)
#     description = models.TextField()
#     # details = JSONField(default=dict)
#     details = models.TextField()
#
#     def __init__(self, *args, **kwargs):
#         models.Model.__init__(self)
#
#     def __str__(self):
#         return name
#
#
# class Buffer(models.Model):
#     ''' convenient copy-paste '''
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#
#     def publish(self):
#         self.created_date = timezone.now()
#         self.save()
