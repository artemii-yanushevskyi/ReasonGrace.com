from django.contrib import admin

from .models import Bookmark
from .models import Purchase

admin.site.register(Bookmark)
admin.site.register(Purchase)
