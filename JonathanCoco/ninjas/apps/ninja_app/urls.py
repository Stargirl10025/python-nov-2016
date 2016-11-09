from django.conf.urls import url
from  . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^ninjas/(?P<ninja>\w*)$', views.ninja)
]
