from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^processPost$', views.processPost),
    url(r'^show_info$', views.show_info)
]
