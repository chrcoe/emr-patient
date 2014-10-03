from django.db import models
 
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager
from django.conf import settings
from django.db import models

class MyUserManager(BaseUserManager):
    def create_user(self, email, twitter_handle, password=None):
        if not email:
            raise ValueError('Users must have an email address')
 
        user = self.model(
            email=MyUserManager.normalize_email(email),
            twitter_handle=twitter_handle,
        )
 
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, email, twitter_handle, password):
        user = self.create_user(email,
            password=password,
            twitter_handle=twitter_handle,
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
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)	
    twitter_handle = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    username_field = 'username'	
    required_field = ['twitter_handle']
		
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

	
class Allergies(models.Model):
    id_patient = models.ForeignKey(Patient)
	allergy_name = models.CharField(max_length=255)
	severity = models.CharField(max_length=255)
	allergy_description = models.CharField(max_length=255)
	def __unicode__(self):
		return self.allergy_description

class LabResults(models.Model):
    id_patient = models.ForeignKey(Patient)
	lab_title = models.CharField(max_length=255)
	lab_date = models.CharField(max_length=255)
	lab_description = models.CharField(max_length=255)
	def __unicode__(self):
		return self.lab_description

class MedicalConditions(models.Model):
    id_patient = models.ForeignKey(Patient)
	condition_name = models.CharField(max_length=255)
	is_family = models.BooleanField(default=False)
	condition_description = models.CharField(max_length=255)
	def __unicode__(self):
		return self.condition_description

class Medication(models.Model):
    id_patient = models.ForeignKey(Patient)
	medication_name = models.CharField(max_length=255)
	dosage = models.IntegerField(default=0)
	medication_description = models.CharField(max_length=255)
	def __unicode__(self):
		return self.medication_description


class Vitals(models.Model):
    id_patient = models.ForeignKey(Patient)
	height_inches = models.IntegerField(default=0)
	weight_pounds = models.IntegerField(default=0)
	blood_pressure = models.IntegerField(default=0)
	pulse = models.IntegerField(default=0)
	def __unicode__(self):
		return self.pulse
