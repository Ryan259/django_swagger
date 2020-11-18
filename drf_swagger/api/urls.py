from django.contrib import admin
from django.conf import settings
from django.urls import path, include

from .views import APIInfoViewSet, APIList, APIDetail

urlpatterns = [
    path('^$', APIInfoViewSet.as_view({'get': 'list'})),
    path('^user/(?P<id>\d+)/$', APIList.as_view())
]
