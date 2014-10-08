from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.db import models


class MyUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=MyUserManager.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email,
                                password=password,
                                )
        user.is_admin = True
        user.save(using=self._db)
        return user

    def get_full_name(self):
        return Patient.first_name, Patient.last_name

    def get_short_name(self):
        return Patient.first_name

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Patient(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    # don't need this, it uses
    # password from AbstractBaseUser
    # password = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(
        ('first_name'), max_length=30, blank=True, null=True)
    last_name = models.CharField(
        ('last_name'), max_length=30, blank=True, null=True)
    phone_num = models.IntegerField(null=True)
    street_address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    zip_code = models.IntegerField(null=True)
    date_of_birth = models.CharField(max_length=255, null=True)
    ssn = models.IntegerField(null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []


class Allergy(models.Model):
    id_patient = models.ForeignKey(Patient)
    allergy_name = models.CharField(max_length=255, null=True)
    severity = models.CharField(max_length=255)
    allergy_description = models.CharField(max_length=255)
    allergy_notes = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.allergy_name


class Appointment(models.Model):
    id_patient = models.ForeignKey(Patient)
    appointment_notes = models.CharField(max_length=255, null=True)
    appointment_date = models.DateTimeField('appointment date')

    def __unicode__(self):
        return self.appoinment_notes


class InsurancePolicy(models.Model):
    id_patient = models.ForeignKey(Patient)
    policy_num = models.CharField(max_length=255)
    exp_date = models.DateTimeField('expiration date')
    comp_name = models.CharField(max_length=255)
    group_num = models.CharField(max_length=255)

    def __unicode__(self):
        return self.policy_num


class LabResult(models.Model):
    id_patient = models.ForeignKey(Patient)
    lab_title = models.CharField(max_length=255)
    lab_date = models.DateTimeField('lab results date')
    lab_description = models.CharField(max_length=255)
    lab_notes = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.lab_title


class MedicalCondition(models.Model):
    id_patient = models.ForeignKey(Patient)
    condition_name = models.CharField(max_length=255)
    is_family = models.BooleanField(default=False)
    condition_description = models.CharField(max_length=255)
    condition_notes = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.condition_description


class Medication(models.Model):
    id_patient = models.ForeignKey(Patient)
    medication_name = models.CharField(max_length=255)
    dosage = models.IntegerField(default=0)
    medication_description = models.CharField(
        max_length=255, null=True, blank=True)
    medication_notes = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.medication_description


class Vital(models.Model):
    id_patient = models.ForeignKey(Patient)
    height_inches = models.IntegerField(default=0)
    weight_pounds = models.IntegerField(default=0)
    blood_pressure = models.IntegerField(default=0)
    pulse = models.IntegerField(default=0)
    vitals_notes = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.pulse
