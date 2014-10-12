#from patient.models import Patient
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from django.contrib.auth import get_user_model
from patient.models import LabResult
# use our custom Patient model (which extends the AbstractBaseUser)
Patient = get_user_model()


def index(request):
    '''This will need to redirect people to the login page in case they visit
    /patient/ directly'''
    return HttpResponse("Hello, world. You're at the PATIENT index.")


def dashboard(request, patient_id):
    # gets the patient object based on the patient_id
    patient = get_object_or_404(Patient, pk=patient_id)
    #gets the dashboard object based on the patient id matching the id passed in
    dashboard = get_object_or_404(dashboard, id_patient=patient_id )
    # renders the page dynamically from the template passed in here (ie: 'patient/dashboard.html')
    # using the dictionary passed to that template: reminder -> dictionary
    # syntax is {'key':value}
    
    return render(request, 'patient/dashboard.html',
                  {'patient': patient, 'dashboard' : dashboard, 'page_name': 'dashboard'})


def vitals(request, patient_id):
    '''function for vitals, uses vitals template'''
    patient = get_object_or_404(Patient, pk=patient_id)
    vitals = get_object_or_404(Vital, id_patient=patient_id)
    return render(request, 'patient/vitals.html',
                  {'patient': patient, 'vitals' : vitals, 'page_name': 'vitals'})


def allergies(request, patient_id):
    '''function for allergies, uses allergies template'''
    patient = get_object_or_404(Patient, pk=patient_id)
    allergies = get_object_or_404(Allergy, id_patient=patient_id)
    return render(request, 'patient/allergies.html',
                  {'patient': patient, 'allergies': allergies, 'page_name': 'allergies'})


def medication(request, patient_id):
    '''function for medication, uses medication template'''
    patient = get_object_or_404(Patient, pk=patient_id)
    medication = get_object_or_404(Medication, id_patient=patient_id)
    return render(request, 'patient/medication.html',
                  {'patient': patient, 'medication' : medication, 'page_name': 'medication'})


def insurance(request, patient_id):
    '''function for insurance, uses insurance template'''
    patient = get_object_or_404(Patient, pk=patient_id)
    insurance = get_object_or_404(InsurancePolicy, id_patient=patient_id)
    return render(request, 'patient/insurance.html',
                  {'patient': patient, 'insurance' : insurance, 'page_name' : 'insurance'})


def conditions(request, patient_id):
    '''function for conditions, uses conditions template'''
    patient = get_object_or_404(Patient, pk=patient_id)
    conditions = get_object_or_404(MedicalCondition, id_patient=patient_id)
    return render(request, 'patient/conditions.html',
                  {'patient': patient, 'conditions' : conditions,'page_name': 'conditions'})


def labresults(request, patient_id):
    '''function for labresults, uses labresults template'''
    patient = get_object_or_404(Patient, pk=patient_id)
    results = get_object_or_404(LabResult, id_patient=patient_id)
    return render(request, 'patient/labresults.html',
                  {'patient': patient, 'results': results, 'page_name': 'labresults'})


def appts(request, patient_id):
    '''function for appts, uses appts template'''
    patient = get_object_or_404(Patient, pk=patient_id)
    appts = get_object_or_404(Appointment, id_patient=patient_id)
    return render(request, 'patient/appts.html',
                  {'patient': patient, 'appts' : appts, 'page_name': 'appts'})


def settings(request, patient_id):
    '''function for settings, uses settings template'''
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(request, 'patient/settings.html',
                  {'patient': patient, 'settings' : settings, 'page_name': 'settings'})
