'''
Created on Nov 25, 2014

@author: chrcoe
'''
from django import forms
from patient.models import Patient


class SettingsForm(forms.Form):

    '''
    Basic Django form class to allow displaying dropdown list of all state
    choices for Settings page on Patient site.
    '''

    CUSTOM_ATTRIB = {'class': 'form-control'}

    state = forms.ChoiceField(
        choices=Patient.STATE_CHOICES,
        widget=forms.Select(attrs=CUSTOM_ATTRIB)
    )
