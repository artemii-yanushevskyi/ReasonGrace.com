from django.contrib import admin

from .models import Bookmark
from .models import Purchase

class PurchaseAdmin(admin.ModelAdmin):
    ''' used to define the fields to display in Djnago admin panel
    (instead of showing purcase(1), purcase(2) etc.)
    '''
    list_display = ('type', 'price')

admin.site.register(Bookmark)
admin.site.register(Purchase, PurchaseAdmin)
