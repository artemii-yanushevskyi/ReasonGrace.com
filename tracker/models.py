from django.db import models

# Create your models here.

from django.db import models 
from django.utils import timezone 

class Post(models.Model): 
    ''' create post class '''
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) 
    title = models.CharField(max_length=200) 
    text = models.TextField() 
    created_date = models.DateTimeField( default=timezone.now)
    published_date = models.DateTimeField( blank=True, null=True) 
    
    def publish(self): 
        self.published_date = timezone.now() 
        self.save() 
    
    def __str__(self): 
        return self.title

class Moment(models.Model):
    ''' create moment class'''
    time = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=500)
    description = models.TextField()
    
    def __init__(self, *args, **kwargs): 
        models.Model.__init__(self)
        self.previous_moments = []
        self.next_moments = []
