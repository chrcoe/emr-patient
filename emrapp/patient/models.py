from django.conf import settings
# from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MaxValueValidator
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db import models
# import datetime


class PatientManager(BaseUserManager):

    def create_user(self, email,
                    #                     first_name, last_name,
                    password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=PatientManager.normalize_email(email),
            #             first_name=first_name,
            #             last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
            self, email,
        #             first_name, last_name,
            password):
        user = self.create_user(
            email=email,
            #             first_name=first_name,
            #             last_name=last_name,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

AlphaValidator = RegexValidator(
    r'^[a-z :A-Z]*$', 'Only letter characters are allowed.')
AlphanumericValidator = RegexValidator(
    r'^[0-9 a-z:A-Z]*$', 'Only alphanumeric characters are allowed.')


class Patient(AbstractBaseUser):
    # http://stackoverflow.com/questions/11351619/
    #     how-to-make-djangos-datetimefield-optional
    email = models.EmailField(max_length=254, unique=True, db_index=True)
    first_name = models.CharField(
        ('First Name'), max_length=30, blank=True, null=True,
        validators=[AlphaValidator])
    last_name = models.CharField(
        ('Last Name'), max_length=30, blank=True, null=True,
        validators=[AlphaValidator])
    phone_num = models.CharField(max_length=12, blank=True, null=True)
    street_address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(
        max_length=255, blank=True, null=True, validators=[AlphaValidator])
    state = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.IntegerField(
        blank=True, null=True, validators=[MaxValueValidator(99999)])
    date_of_birth = models.DateField(blank=True, null=True)
    ssn = models.IntegerField(
        blank=True, null=True, validators=[MaxValueValidator(999999999)])

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = PatientManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []

    def get_full_name(self):
        return self.email
#         return '{} {}'.format(Patient.first_name, Patient.last_name)

    def get_short_name(self):
        return self.email
#         return Patient.first_name

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Allergy(models.Model):
    id_patient = models.ForeignKey(settings.AUTH_USER_MODEL)
    allergy_name = models.CharField(
        max_length=255, null=True, validators=[AlphaValidator])
    severity = models.CharField(
        max_length=255, validators=[AlphanumericValidator])
    allergy_description = models.CharField(
        max_length=255, validators=[AlphanumericValidator])
    allergy_notes = models.CharField(
        max_length=255, blank=True, validators=[AlphanumericValidator])

    def __unicode__(self):
        return self.allergy_name

    class Meta:
        verbose_name = 'Allergy'
        verbose_name_plural = 'Allergies'


class Appointment(models.Model):
    id_patient = models.ForeignKey(settings.AUTH_USER_MODEL)
    appointment_notes = models.CharField(
        max_length=255, null=True, validators=[AlphanumericValidator])
    appointment_date = models.DateField('appointment date')

    def __unicode__(self):
        return self.appointment_notes


class InsurancePolicy(models.Model):
    id_patient = models.ForeignKey(settings.AUTH_USER_MODEL)
    policy_num = models.CharField(
        max_length=255, validators=[AlphanumericValidator])
    exp_date = models.DateField('expiration date')
    comp_name = models.CharField(
        max_length=255, validators=[AlphanumericValidator])
    group_num = models.CharField(
        max_length=255, validators=[AlphanumericValidator])

    def __unicode__(self):
        return self.policy_num

    class Meta:
        verbose_name = 'Insurance Policy'
        verbose_name_plural = 'Insurance Policies'


class DiagnosticResult(models.Model):
    id_patient = models.ForeignKey(settings.AUTH_USER_MODEL)
    lab_title = models.CharField(max_length=255)
    lab_date = models.DateField('lab results date')
    lab_description = models.CharField(max_length=255)
    lab_notes = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.lab_title


class MedicalHistory(models.Model):
    id_patient = models.ForeignKey(settings.AUTH_USER_MODEL)
    history_item_name = models.CharField(max_length=255)
    is_family_item = models.BooleanField(default=False)
    history_item_date = models.DateField('Diagnosis date of History Item')
    history_description = models.CharField(max_length=255)
    history_notes = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.history_item_name

    class Meta:
        verbose_name = 'Medical History'
        verbose_name_plural = 'Medical History'


class Medication(models.Model):
    id_patient = models.ForeignKey(settings.AUTH_USER_MODEL)
    medication_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)
    medication_description = models.CharField(
        max_length=255, null=True, blank=True)
    medication_notes = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.medication_description


class Vital(models.Model):
    id_patient = models.ForeignKey(settings.AUTH_USER_MODEL)
    height_inches = models.IntegerField(null=True, blank=True)
    weight_pounds = models.IntegerField(null=True, blank=True)
    bp_sys = models.IntegerField(null=True, blank=True)
    bp_dias = models.IntegerField(null=True, blank=True)
    pulse = models.IntegerField(null=True, blank=True)
    vitals_date = models.DateField('vitals date', null=True, blank=True)
    vitals_notes = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.pulse)
