from django.contrib import admin
from .models import Post
from .models import Buffer
from .models import Bookmark
# Register your models here.
admin.site.register(Post)
admin.site.register(Buffer)
admin.site.register(Bookmark)
