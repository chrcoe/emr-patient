#from patient.models import Patient
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, get_list_or_404
from django.shortcuts import render

from patient.models import Allergy
from patient.models import Appointment
from patient.models import InsurancePolicy
from patient.models import DiagnosticResult
from patient.models import MedicalHistory
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
    if patient.is_admin or patient.is_staff:
        return redirect('/admin/')
    vitals = get_list_or_404(Vital, id_patient=patient_id)
    medication = get_list_or_404(Medication, id_patient=patient_id)
    appts = get_list_or_404(Appointment, id_patient=patient_id)
    diagnosticresults = get_list_or_404(DiagnosticResult, id_patient=patient_id)
    allergies = get_list_or_404(Allergy, id_patient=patient_id)
    insurance = get_list_or_404(InsurancePolicy, id_patient=patient_id)
    conditions = get_list_or_404(MedicalHistory, id_patient=patient_id)
    return render(request, 'patient/dashboard.html',
                  {'patient': patient, 'vitals': vitals, 'medication': medication, 'appts': appts, 'diagnosticresults': diagnosticresults, 'allergies': allergies, 'insurance': insurance, 'conditions': conditions,
                   'page_name': 'Dashboard'})


@login_required
def vitals(request, patient_id):
    '''function for vitals, uses vitals template'''
    if request.user.id <> patient_id:
        patient_id = request.user.id
    patient = get_object_or_404(Patient, pk=patient_id)
    if patient.is_admin or patient.is_staff:
        return redirect('/admin/')
    vitals = get_list_or_404(Vital, id_patient=patient_id)

    # need to handle the POST data for all notes
    if request.method == 'POST':
        #         posted = request.POST
        for i in vitals:
            # update ONLY the notes that the patient wanted to update
            if i.id == int(request.POST['vitals_id']):
                # set the notes on THIS record to the new notes
                i.vitals_notes = request.POST['vitals_notes']
                # save changes to the DB
                i.save()

    return render(request, 'patient/vitals.html',
                  {'patient': patient, 'vitals': vitals, 'page_name': 'Vitals'})


@login_required
def allergies(request, patient_id):
    '''function for allergies, uses allergies template'''
    if request.user.id <> patient_id:
        patient_id = request.user.id
    patient = get_object_or_404(Patient, pk=patient_id)
    if patient.is_admin or patient.is_staff:
        return redirect('/admin/')
    allergies = get_list_or_404(Allergy, id_patient=patient_id)
    return render(request, 'patient/allergies.html',
                  {'patient': patient, 'allergies': allergies, 'page_name': 'Allergies'})


@login_required
def medication(request, patient_id):
    '''function for medication, uses medication template'''
    if request.user.id <> patient_id:
        patient_id = request.user.id
    patient = get_object_or_404(Patient, pk=patient_id)
    medication = get_list_or_404(Medication, id_patient=patient_id)
    if patient.is_admin or patient.is_staff:
        return redirect('/admin/')
    return render(request, 'patient/medication.html',
                  {'patient': patient, 'medication': medication, 'page_name': 'Medication'})


@login_required
def insurance(request, patient_id):
    '''function for insurance, uses insurance template'''
    if request.user.id <> patient_id:
        patient_id = request.user.id
    patient = get_object_or_404(Patient, pk=patient_id)
    if patient.is_admin or patient.is_staff:
        return redirect('/admin/')
    insurance = get_list_or_404(InsurancePolicy, id_patient=patient_id)
    return render(request, 'patient/insurance.html',
                  {'patient': patient, 'insurance': insurance, 'page_name': 'Insurance Policies'})


@login_required
def conditions(request, patient_id):
    '''function for conditions, uses conditions template'''
    if request.user.id <> patient_id:
        patient_id = request.user.id
    patient = get_object_or_404(Patient, pk=patient_id)
    if patient.is_admin or patient.is_staff:
        return redirect('/admin/')
    conditions = get_list_or_404(MedicalHistory, id_patient=patient_id)
    return render(request, 'patient/conditions.html',
                  {'patient': patient, 'conditions': conditions, 'page_name': 'Medical History'})


@login_required
def diagnosticresults(request, patient_id):
    '''function for labresults, uses labresults template'''
    if request.user.id <> patient_id:
        patient_id = request.user.id
    patient = get_object_or_404(Patient, pk=patient_id)
    if patient.is_admin or patient.is_staff:
        return redirect('/admin/')
    diagnosticresults = get_list_or_404(DiagnosticResult, id_patient=patient_id)
    return render(request, 'patient/diagnosticresults.html',
                  {'patient': patient, 'diagnosticresults': diagnosticresults, 'page_name': 'Diagnostic Results'})


@login_required
def appts(request, patient_id):
    '''function for appts, uses appts template'''
    if request.user.id <> patient_id:
        patient_id = request.user.id
    patient = get_object_or_404(Patient, pk=patient_id)
    if patient.is_admin or patient.is_staff:
        return redirect('/admin/')
    appts = get_list_or_404(Appointment, id_patient=patient_id)
    return render(request, 'patient/appts.html',
                  {'patient': patient, 'appts': appts, 'page_name': 'Appointments'})


@login_required
def settings(request, patient_id):
    '''function for settings, uses settings template'''
    if request.user.id <> patient_id:
        patient_id = request.user.id
    patient = get_object_or_404(Patient, pk=patient_id)
    if patient.is_admin or patient.is_staff:
        return redirect('/admin/')
    return render(request, 'patient/settings.html',
                  {'patient': patient, 'settings': settings, 'page_name': 'Settings'})
