from django.contrib import admin
from patient.models import Vital, Patient, Appointment, InsurancePolicy,\
    LabResult, MedicalCondition, Medication, Allergy

# Register your models here.
admin.site.register(Patient)
admin.site.register(Allergy)
admin.site.register(Appointment)
admin.site.register(InsurancePolicy)
admin.site.register(LabResult)
admin.site.register(MedicalCondition)
admin.site.register(Medication)
admin.site.register(Vital)
