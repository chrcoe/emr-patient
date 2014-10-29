from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from patient.models import Vital, Patient, Appointment, InsurancePolicy,\
    DiagnosticResult, MedicalHistory, Medication, Allergy

# http://stackoverflow.com/questions/15456964/changing-password-in-django-admin


class PatientCreationForm(forms.ModelForm):

    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Patient
        fields = (
            'email',
            'date_of_birth',
            'first_name',
            'last_name',
            'ssn'
        )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(PatientCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class PatientChangeForm(forms.ModelForm):

    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField(
        label=("Password"),
        help_text= ("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"password/\">this form</a>."))

    class Meta:
        model = Patient
        fields = (
            'email',
            'first_name',
            'last_name',
            'phone_num',
            'street_address',
            'city',
            'state',
            'zip_code',
            'date_of_birth',
            'ssn',
            'is_active',
            'is_staff',
            'is_admin',
        )

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class VitalsInline(admin.TabularInline):
    model = Vital
    extra = 1

class AllergyInline(admin.TabularInline):
    model = Allergy
    extra = 1

class AppointmentInline(admin.TabularInline):
    model = Appointment
    extra = 1

class InsuranceInline(admin.TabularInline):
    model = InsurancePolicy
    extra = 1

class DiagResultsInline(admin.TabularInline):
    model = DiagnosticResult
    extra = 1

class MedHisInline(admin.TabularInline):
    model = MedicalHistory
    extra = 1

class MedicationInline(admin.TabularInline):
    model = Medication
    extra = 1

class PatientAdmin(UserAdmin):
    # The forms to add and change user instances
    form = PatientChangeForm
    add_form = PatientCreationForm



    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = (
        'email', 'date_of_birth', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': (
            'date_of_birth',
            'first_name',
            'last_name',
            'ssn',
            'phone_num',
            'street_address',
            'city',
            'state',
            'zip_code',
        ), 'classes' : ['collapse']}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 'is_staff'), 'classes' : ['collapse']}),
        ('Important dates', {'fields': ('last_login',), 'classes' : ['collapse']}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'ssn', 'first_name',
                       'last_name', 'password1', 'password2',
                       'is_admin', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

    inlines = [VitalsInline, AllergyInline, AppointmentInline, InsuranceInline,
               DiagResultsInline, MedHisInline, MedicationInline, ]


# Register your models here.
admin.site.register(Patient, PatientAdmin)
