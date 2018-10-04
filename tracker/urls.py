from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.site_report, name='site_report'),
    path('about', views.site_report),
    path('unicode', views.unicode_test),

    re_path(r'encode/?$', views.encode_page),
    re_path(r'encode/(?P<username>[\w-]*)/?$', views.encode_page),

    re_path(r'shop/?$', views.shop_dash, name='shop_dash'),
    re_path(r'shop/(?P<seller>[\s\w-]*)/?$', views.shop_dash, name='shop_dash'),

    re_path(r'shop-qr/(?P<seller>[\s\w-]*)/$', views.shop_qr, name='shop_qr'),
    ''' example links:
    http://reasongrace.com/shop-qr/Гоша%20Вор/?price=12&type=Kit%20Kat
    http://reasongrace.com/shop-qr/Derek/?price=2000&type=Виза
    '''
]
