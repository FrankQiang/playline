from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
   url(r'^$', 'playline.views.home', name='home'),
   url(r'^admin/', include(admin.site.urls)),
   url(r'^search/', include('haystack.urls')),
   url('', include('social.apps.django_app.urls', namespace='social')),
   url('', include('django.contrib.auth.urls', namespace='auth')),
]
