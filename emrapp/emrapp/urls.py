from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from emrapp import views

urlpatterns = patterns('',
   # Examples:
   # url(r'^$', 'emrapp.views.home', name='home'),
   # url(r'^blog/', include('blog.urls')),

   # points to base index page (emrapp/views.py etc.)
   url(r'^$', views.login, name='login'),
   # built in admin page
   url(r'^admin/', include(admin.site.urls)),
   # additional app pages go here (ie: patient app etc)
   url(r'^patient/',
       include('patient.urls', namespace='patient')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
