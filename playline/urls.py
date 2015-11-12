from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
   url(r'^$', 'playline.views.home', name='home'),
   url(r'^error/$', 'playline.views.error', name='error'),
   url(r'^about/$', 'playline.views.about', name='about'),
   url(r'^user/(\d+)/$', 'playline.views.user', name='user'),
   url(r'^school/', include('school.urls', namespace="school")),
   url(r'^admin/', include(admin.site.urls)),
   url(r'^search/', include('haystack.urls')),
   url('', include('social.apps.django_app.urls', namespace='social')),
   url('', include('django.contrib.auth.urls', namespace='auth')),
]
