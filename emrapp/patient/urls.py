from django.conf.urls import patterns, url

from patient import views

urlpatterns = patterns('',
#    url(r'^$', views.index, name='index'),

    # /patient/patient_id/
    url(r'^(?P<patient_id>\d+)/$', views.dashboard, name='dashboard'), # after the patient logs in, you do not need to build this view yet

    # /patient/patient_id/vitals/
    url(r'^(?P<patient_id>\d+)/vitals/$', views.vitals, name='vitals'), # this calls the views.vitals() function when this link is requested

    # /patient/patient_id/allergies/
    url(r'^(?P<patient_id>\d+)/allergies/$', views.allergies, name='allergies'), # this calls the views.allergies() function when this link is requested

    # /patient/patient_id/medication/
    url(r'^(?P<patient_id>\d+)/medication/$', views.medication, name='medication'), # this calls the views.medication() function when this link is requested

    # /patient/patient_id/insurance/
    url(r'^(?P<patient_id>\d+)/insurance/$', views.insurance, name='insurance'), # this calls the views.insurance() function when this link is requested

    # /patient/patient_id/conditions/
    url(r'^(?P<patient_id>\d+)/medicalHistory/$', views.medicalHistory, name='medicalHistory'), # this calls the views.conditions() function when this link is requested

    # /patient/patient_id/diagnosticresults/
    url(r'^(?P<patient_id>\d+)/diagnosticresults/$', views.diagnosticresults, name='diagnosticresults'), # this calls the views.labresults() function when this link is requested

    # /patient/patient_id/appts/
    url(r'^(?P<patient_id>\d+)/appts/$', views.appts, name='appts'), # this calls the views.appts() function when this link is requested

     # /patient/patient_id/settings/
    url(r'^(?P<patient_id>\d+)/settings/$', views.settings, name='settings'), # this calls the views.settings() function when this link is requested

)
