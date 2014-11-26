from django.conf import settings
from django.core.validators import RegexValidator, MaxValueValidator
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db import models


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

    STATE_CHOICES = (
        ('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'),
        ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'),
        ('CT', 'Connecticut'), ('DE', 'Delaware'), ('FL', 'Florida'),
        ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'),
        ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'),
        ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'),
        ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'),
        ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'),
        ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'),
        ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'),
        ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'),
        ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'),
        ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'),
        ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )

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
    state = models.CharField(
        max_length=255, blank=True, null=True, choices=STATE_CHOICES
    )
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

    SEVERITY_CHOICES = (
        ('1', 'Mild'),
        ('2', 'Mild - Moderate'),
        ('3', 'Moderate'),
        ('4', 'Moderate - Severe'),
        ('5', 'Severe'),
    )

    id_patient = models.ForeignKey(settings.AUTH_USER_MODEL)
    allergy_name = models.CharField(
        max_length=255, null=True, validators=[AlphaValidator])
    severity = models.CharField(
        max_length=255, validators=[AlphanumericValidator],
        choices=SEVERITY_CHOICES
    )
    allergy_description = models.CharField(
        max_length=255, validators=[AlphanumericValidator])
    allergy_date = models.DateField('Date of allergy diagnosis')
    allergy_notes = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.allergy_name

    class Meta:
        verbose_name = 'Allergy'
        verbose_name_plural = 'Allergies'
        ordering = ['-allergy_date']


class Appointment(models.Model):

    TYPE_CHOICES = (
        ('OV', 'Office Visit'),
        ('CPX', 'Annual Physical'),
        ('WC', 'Well Child'),
        ('NV', 'Nurse Visit'),
        ('AI', 'Allergy Injection'),
        ('PAT', 'Pre-Admission Testing'),
        ('PAP', 'PAP'),
        ('BLDWK', 'Blood Work'),
        ('FU', 'Hospital Followup'),
        ('DEXA', 'Bone Density Scan'),
        ('NP', 'New Patient'),
    )

    id_patient = models.ForeignKey(settings.AUTH_USER_MODEL)
    appointment_type = models.CharField(
        max_length=255, null=True, choices=TYPE_CHOICES
    )
    appointment_description = models.CharField(max_length=255, null=True)
    appointment_date = models.DateField('Date of appointment')
    appointment_notes = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.appointment_type

    class Meta:
        ordering = ['-appointment_date']


class InsurancePolicy(models.Model):
    id_patient = models.ForeignKey(settings.AUTH_USER_MODEL)
    policy_num = models.CharField(
        max_length=255, validators=[AlphanumericValidator])
    comp_name = models.CharField('Company Name',
                                 max_length=255, validators=[AlphanumericValidator])
    group_num = models.CharField(
        max_length=255, validators=[AlphanumericValidator])
    exp_date = models.DateField('expiration date')

    def __unicode__(self):
        return self.policy_num

    class Meta:
        verbose_name = 'Insurance Policy'
        verbose_name_plural = 'Insurance Policies'
        ordering = ['-exp_date']


class DiagnosticResult(models.Model):
    id_patient = models.ForeignKey(settings.AUTH_USER_MODEL)
    result_title = models.CharField(max_length=255)
    result_description = models.CharField(max_length=255)
    result_date = models.DateField('date of result')
    result_notes = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.result_title

    class Meta:
        ordering = ['-result_date']


class MedicalHistory(models.Model):
    id_patient = models.ForeignKey(settings.AUTH_USER_MODEL)
    history_item_name = models.CharField(max_length=255)
    is_family_item = models.BooleanField(default=False)
    history_description = models.CharField(max_length=255)
    history_item_date = models.DateField('Diagnosis date of History Item')
    history_notes = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.history_item_name

    class Meta:
        verbose_name = 'Medical History'
        verbose_name_plural = 'Medical History'
        ordering = ['-history_item_date']


class Medication(models.Model):
    id_patient = models.ForeignKey(settings.AUTH_USER_MODEL)
    medication_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)
    medication_description = models.CharField(
        max_length=255, null=True, blank=True)
    medication_date = models.DateField('Date of Perscription')
    medication_notes = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.medication_description

    class Meta:
        ordering = ['-medication_date']


class Vital(models.Model):
    id_patient = models.ForeignKey(settings.AUTH_USER_MODEL)
    height_inches = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True)
    weight_pounds = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    bp_sys = models.IntegerField(null=True, blank=True)
    bp_dias = models.IntegerField(null=True, blank=True)
    pulse = models.IntegerField(null=True, blank=True)
    vitals_date = models.DateField('vitals date', null=True, blank=True)
    vitals_notes = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.pulse)

    class Meta:
        ordering = ['-vitals_date']
