from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from patient.forms import SettingsForm
from patient.models import Allergy
from patient.models import Appointment
from patient.models import DiagnosticResult
from patient.models import InsurancePolicy
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
    vitals = list(Vital.objects.filter(id_patient=patient_id))
    medication = list(Medication.objects.filter(id_patient=patient_id))
    appts = list(Appointment.objects.filter(id_patient=patient_id))
    diagnosticresults = list(
        DiagnosticResult.objects.filter(id_patient=patient_id))
    allergies = list(Allergy.objects.filter(id_patient=patient_id))
    insurance = list(InsurancePolicy.objects.filter(id_patient=patient_id))
    medicalHistory = list(MedicalHistory.objects.filter(id_patient=patient_id))
    return render(request, 'patient/dashboard.html',
                  {'patient': patient, 'vitals': vitals, 'medication': medication, 'appts': appts, 'diagnosticresults': diagnosticresults, 'allergies': allergies, 'insurance': insurance, 'medicalHistory': medicalHistory,
                   'page_name': 'Dashboard'})


@csrf_protect
@login_required
def vitals(request, patient_id):
    '''function for vitals, uses vitals template'''
    if request.user.id <> patient_id:
        patient_id = request.user.id
    patient = get_object_or_404(Patient, pk=patient_id)
    if patient.is_admin or patient.is_staff:
        return redirect('/admin/')
    data = list(Vital.objects.filter(id_patient=patient_id))

    # need to handle the POST data for all notes
    if request.method == 'POST':
        #         posted = request.POST
        for i in data:
            # update ONLY the notes that the patient wanted to update
            if i.id == int(request.POST['vitals_id']):
                # set the notes on THIS record to the new notes
                i.vitals_notes = request.POST['vitals_notes']
                # save changes to the DB
                i.save()

    return render(request, 'patient/vitals.html',
                  {'patient': patient, 'data': data, 'page_name': 'Vitals'})


@csrf_protect
@login_required
def allergies(request, patient_id):
    '''function for allergies, uses allergies template'''
    if request.user.id <> patient_id:
        patient_id = request.user.id
    patient = get_object_or_404(Patient, pk=patient_id)
    if patient.is_admin or patient.is_staff:
        return redirect('/admin/')
    data = list(Allergy.objects.filter(id_patient=patient_id))

    # need to handle the POST data for all notes
    if request.method == 'POST':
        #         posted = request.POST
        for i in data:
            # update ONLY the notes that the patient wanted to update
            if i.id == int(request.POST['allergies_id']):
                # set the notes on THIS record to the new notes
                i.allergy_notes = request.POST['allergy_notes']
                # save changes to the DB
                i.save()

    return render(request, 'patient/allergies.html',
                  {'patient': patient, 'data': data, 'page_name': 'Allergies'})


@csrf_protect
@login_required
def medication(request, patient_id):
    '''function for medication, uses medication template'''
    if request.user.id <> patient_id:
        patient_id = request.user.id
    patient = get_object_or_404(Patient, pk=patient_id)
    data = list(Medication.objects.filter(id_patient=patient_id))
    if patient.is_admin or patient.is_staff:
        return redirect('/admin/')

    # need to handle the POST data for all notes
    if request.method == 'POST':
        #         posted = request.POST
        for i in data:
            # update ONLY the notes that the patient wanted to update
            if i.id == int(request.POST['medication_id']):
                # set the notes on THIS record to the new notes
                i.medication_notes = request.POST['medication_notes']
                # save changes to the DB
                i.save()

    return render(request, 'patient/medication.html',
                  {'patient': patient, 'data': data, 'page_name': 'Medication'})


@csrf_protect
@login_required
def insurance(request, patient_id):
    '''function for insurance, uses insurance template'''
    if request.user.id <> patient_id:
        patient_id = request.user.id
    patient = get_object_or_404(Patient, pk=patient_id)
    if patient.is_admin or patient.is_staff:
        return redirect('/admin/')
    data = list(InsurancePolicy.objects.filter(id_patient=patient_id))

# need to handle the POST data for all notes
#     if request.method == 'POST':
# posted = request.POST
#         for i in data:
# update ONLY the notes that the patient wanted to update
#             if i.id == int(request.POST['insurance_id']):
# set the notes on THIS record to the new notes
#                 i.insurance_notes = request.POST['insurance_notes']
# save changes to the DB
#                 i.save()

    return render(request, 'patient/insurance.html',
                  {'patient': patient, 'data': data, 'page_name': 'Insurance Policies'})


@csrf_protect
@login_required
def medicalHistory(request, patient_id):
    '''function for medicalHistory, uses medicalHistory template'''
    if request.user.id <> patient_id:
        patient_id = request.user.id
    patient = get_object_or_404(Patient, pk=patient_id)
    if patient.is_admin or patient.is_staff:
        return redirect('/admin/')
    data = list(MedicalHistory.objects.filter(id_patient=patient_id))

    # need to handle the POST data for all notes
    if request.method == 'POST':
        #         posted = request.POST
        for i in data:
            # update ONLY the notes that the patient wanted to update
            if i.id == int(request.POST['history_id']):
                # set the notes on THIS record to the new notes
                i.history_notes = request.POST['history_notes']
                # save changes to the DB
                i.save()

    return render(request, 'patient/medicalHistory.html',
                  {'patient': patient, 'data': data, 'page_name': 'Medical History'})


@csrf_protect
@login_required
def diagnosticresults(request, patient_id):
    '''function for diagnosticresults, uses diagnosticresults template'''
    if request.user.id <> patient_id:
        patient_id = request.user.id
    patient = get_object_or_404(Patient, pk=patient_id)
    if patient.is_admin or patient.is_staff:
        return redirect('/admin/')
    data = list(
        DiagnosticResult.objects.filter(id_patient=patient_id))

    # need to handle the POST data for all notes
    if request.method == 'POST':
        #         posted = request.POST
        for i in data:
            # update ONLY the notes that the patient wanted to update
            if i.id == int(request.POST['result_id']):
                # set the notes on THIS record to the new notes
                i.result_notes = request.POST['result_notes']
                # save changes to the DB
                i.save()

    return render(request, 'patient/diagnosticresults.html',
                  {'patient': patient, 'data': data, 'page_name': 'Diagnostic Results'})


@csrf_protect
@login_required
def appts(request, patient_id):
    '''function for appts, uses appts template'''
    if request.user.id <> patient_id:
        patient_id = request.user.id
    patient = get_object_or_404(Patient, pk=patient_id)
    if patient.is_admin or patient.is_staff:
        return redirect('/admin/')
    data = list(Appointment.objects.filter(id_patient=patient_id))

    # need to handle the POST data for all notes
    if request.method == 'POST':
        #         posted = request.POST
        for i in data:
            # update ONLY the notes that the patient wanted to update
            if i.id == int(request.POST['appts_id']):
                # set the notes on THIS record to the new notes
                i.appointment_notes = request.POST['appts_notes']
                # save changes to the DB
                i.save()

    return render(request, 'patient/appts.html',
                  {'patient': patient, 'data': data, 'page_name': 'Appointments'})


@csrf_protect
@login_required
def settings(request, patient_id):
    '''function for settings, uses settings template'''
    if request.user.id <> patient_id:
        patient_id = request.user.id
    patient = get_object_or_404(Patient, pk=patient_id)
    if patient.is_admin or patient.is_staff:
        return redirect('/admin/')

    settings_form = SettingsForm(initial= {'state': patient.state})
    pw_form = PasswordChangeForm(user=request.user)
    errMsg = ''
    successMsg = ''
    pwSuccessMsg = ''
    # need to handle the POST data for all info
    if request.method == 'POST':
        if 'is_changing_demographics' in request.POST:
            # set the info on THIS record to the new info
            if 'phone_num' in request.POST:
                patient.phone_num = request.POST['phone_num']
            if 'street_address' in request.POST:
                patient.street_address = request.POST['street_address']
            if 'city' in request.POST:
                patient.city = request.POST['city']
            if 'state' in request.POST:
                patient.state = request.POST['state']
            if 'zip_code' in request.POST:
                patient.zip_code = request.POST['zip_code']
            # save changes to the DB
            patient.save()
            # change the displayed default to the new current state
            settings_form.initial = {'state': patient.state}
            successMsg = 'Saved changes.'

        if 'is_changing_password' in request.POST:
            pw_form = PasswordChangeForm(user=request.user, data=request.POST)
            if pw_form.is_valid():
                pw_form.save()
                # Updating the password logs out all other sessions for the user
                # except the current one if
                # django.contrib.auth.middleware.SessionAuthenticationMiddleware
                # is enabled.
                update_session_auth_hash(request, pw_form.user)
                pwSuccessMsg = 'Password successfully updated.'
    #             return HttpResponseRedirect(post_change_redirect)

    return render(request, 'patient/settings.html',
                  {'patient': patient, 'settings': settings,
                   'page_name': 'Settings', 'pw_form': pw_form,
                   'settings_form':settings_form,
                   'errMsg': errMsg, 'successMsg': successMsg,
                   'pwSuccessMsg': pwSuccessMsg})
