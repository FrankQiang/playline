from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.new, name='new'),
    url(r'^show/(\d+)$', views.show, name='show'),
    url(r'^accept/(\d+)$', views.accept, name='accept'),
    url(r'^delete/(\d+)$', views.delete, name='delete'),
]