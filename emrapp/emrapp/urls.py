from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
# from django.contrib.auth.views import password_reset
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from emrapp import views
urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'emrapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # points to base index page (emrapp/views.py etc.)
    url(r'^$', views.login_page, {'success_msg' : None},
        name='login'),
    # built in admin page
    url(r'^admin/', include(admin.site.urls)),
    # additional app pages go here (ie: patient app etc)
    url(r'^patient/', include('patient.urls', namespace='patient')),
    url(r'^logout/', views.logout_page, name='logout'),
    url(r'^success/$', views.login_page, {'success_msg' : 'Instructions sent to your inbox.'},
        name='password_change_sent'),
    url(r'^reset/login/$', views.login_page, {'success_msg' : 'Password reset, you may now login.'},
        name='password_reset_complete'),

    url(r'^reset/$',
        'django.contrib.auth.views.password_reset',
        {'post_reset_redirect' : '/success'},
        name="password_reset"),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
