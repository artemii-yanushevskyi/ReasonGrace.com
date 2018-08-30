from django.urls import path
from . import views

urlpatterns = [
    path('', views.tracker_data, name='tracker_data'),
    path('dynamic', views.dynamic_update),
    path('bookmarks', views.bookmarks_display),
    path('about', views.site_report),
]
