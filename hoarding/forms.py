from django import forms
from django.forms import ModelForm
from hoarding.models import Hoarding

class HoardingForm(ModelForm):
    
    class Meta:
        model   = Hoarding
        exclude = ('user', 'enabled', 'deleted', 'created', 'updated', 'comment')
    
   
    
    