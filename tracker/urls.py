from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.site_report, name='site_report'),
    path('about', views.site_report),
    path('unicode', views.unicode_test),
    
    re_path(r'encode/?$',views.encode_page),
    re_path(r'encode/(?P<username>[\w-]*)/?$', views.encode_page),

    re_path(r'shop/?$',views.shop_dash, name='shop_dash'),
    re_path(r'shop/(?P<seller>[\w-]*)/?$', views.shop_dash, name='shop_dash'),
]
