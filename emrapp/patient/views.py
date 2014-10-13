#from patient.models import Patient
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from patient.models import Allergy
from patient.models import Appointment
from patient.models import InsurancePolicy
from patient.models import LabResult
from patient.models import MedicalCondition
from patient.models import Medication
from patient.models import Vital
# use our custom Patient model (which extends the AbstractBaseUser)
Patient = get_user_model()


@login_required
def dashboard(request, patient_id):
    # check current id matches the requested id
    # (prevent user from accessing other user's info)
    if request.user.id <> patient_id:
        patient_id = request.user.id
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(request, 'patient/dashboard.html',
                  {'patient': patient,
                   'page_name': 'Dashboard'})


@login_required
def vitals(request, patient_id):
    '''function for vitals, uses vitals template'''
    if request.user.id <> patient_id:
        patient_id = request.user.id
    patient = get_object_or_404(Patient, pk=patient_id)
    vitals = get_object_or_404(Vital, id_patient=patient_id)
    return render(request, 'patient/vitals.html',
                  {'patient': patient, 'vitals': vitals, 'page_name': 'Vitals'})


@login_required
def allergies(request, patient_id):
    '''function for allergies, uses allergies template'''
    if request.user.id <> patient_id:
        patient_id = request.user.id
    patient = get_object_or_404(Patient, pk=patient_id)
    allergies = get_object_or_404(Allergy, id_patient=patient_id)
    return render(request, 'patient/allergies.html',
                  {'patient': patient, 'allergies': allergies, 'page_name': 'Allergies'})


@login_required
def medication(request, patient_id):
    '''function for medication, uses medication template'''
    if request.user.id <> patient_id:
        patient_id = request.user.id
    patient = get_object_or_404(Patient, pk=patient_id)
    medication = get_object_or_404(Medication, id_patient=patient_id)
    return render(request, 'patient/medication.html',
                  {'patient': patient, 'medication': medication, 'page_name': 'Medication'})


@login_required
def insurance(request, patient_id):
    '''function for insurance, uses insurance template'''
    if request.user.id <> patient_id:
        patient_id = request.user.id
    patient = get_object_or_404(Patient, pk=patient_id)
    insurance = get_object_or_404(InsurancePolicy, id_patient=patient_id)
    return render(request, 'patient/insurance.html',
                  {'patient': patient, 'insurance': insurance, 'page_name': 'Insurance Policies'})


@login_required
def conditions(request, patient_id):
    '''function for conditions, uses conditions template'''
    if request.user.id <> patient_id:
        patient_id = request.user.id
    patient = get_object_or_404(Patient, pk=patient_id)
    conditions = get_object_or_404(MedicalCondition, id_patient=patient_id)
    return render(request, 'patient/conditions.html',
                  {'patient': patient, 'conditions': conditions, 'page_name': 'Medical Conditions'})


@login_required
def labresults(request, patient_id):
    '''function for labresults, uses labresults template'''
    if request.user.id <> patient_id:
        patient_id = request.user.id
    patient = get_object_or_404(Patient, pk=patient_id)
    labresults = get_object_or_404(LabResult, id_patient=patient_id)
    return render(request, 'patient/labresults.html',
                  {'patient': patient, 'labresults': labresults, 'page_name': 'Lab Results'})


@login_required
def appts(request, patient_id):
    '''function for appts, uses appts template'''
    if request.user.id <> patient_id:
        patient_id = request.user.id
    patient = get_object_or_404(Patient, pk=patient_id)
    appts = get_object_or_404(Appointment, id_patient=patient_id)
    return render(request, 'patient/appts.html',
                  {'patient': patient, 'appts': appts, 'page_name': 'Appointments'})


@login_required
def settings(request, patient_id):
    '''function for settings, uses settings template'''
    if request.user.id <> patient_id:
        patient_id = request.user.id
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(request, 'patient/settings.html',
                  {'patient': patient, 'settings': settings, 'page_name': 'Settings'})
