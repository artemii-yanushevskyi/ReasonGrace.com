from django.db import models
from django.utils import timezone

class Purchase(models.Model):
    type = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    time = models.DateTimeField(default=timezone.now)
    seller = models.CharField(max_length=10)

    def __str__(self):
<<<<<<< HEAD
=======
        type = self.type
        price = self.price
>>>>>>> a9fdc75233ae79c732e1298da3b81a0bdd308c1e
        return ' | '.join([self.type, self.price, self.time, self.seller])


class Bookmark(models.Model):
    ''' create bookmark'''
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

