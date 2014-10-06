from django.shortcuts import render get_object_or_404
from django.http import HttpResponse

def index(request):
        return HttpResponse("Hello, world. You're at the PATIENT index.")

def dashboard(request, patient_id):
    # gets the patient object based on the patient_id
    patient = get_object_or_404(Patient, pk=patient_id)
    # renders the page dynamically from the template passed in here (ie: 'patient/dashboard.html')
    # using the dictionary passed to that template: reminder -> dictionary syntax is {'key':value}
    return render(request, 'patient/dashboard.html', {'patient': patient, 'page_name':'DASHBOARD'})

# function for vitals, uses vitals template
def vitals(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(request, 'patient/vitals.html', {'patient': patient, 'page_name':'VITALS'})

# function for allergies, uses allergies template
def allergies(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(request, 'patient/allergies.html', {'patient': patient, 'page_name':'allergies'})

# function for medication, uses medication template
def medication(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(request, 'patient/medication.html', {'patient': patient, 'page_name':'medication'})

# function for insurance, uses insurance template
def insurance(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(request, 'patient/insurance.html', {'patient': patient, 'page_name':'insurance'})

# function for conditions, uses conditions template
def conditions(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(request, 'patient/conditions.html', {'patient': patient, 'page_name':'conditions'})

# function for labresults, uses labresults template
def labresults(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(request, 'patient/labresults.html', {'patient': patient, 'page_name':'labresults'})

# function for appts, uses appts template
def appts(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(request, 'patient/appts.html', {'patient': patient, 'page_name':'appts'})

