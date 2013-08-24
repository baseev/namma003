from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from hoardingusers.models import UserInfo

class RegistrationForm(ModelForm):
    
    username    = forms.CharField(label=(u'User Name'))
    email       = forms.EmailField(label=(u'Email Address'))
    password1   = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False)) 
    password    = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))    
    
    
    class Meta:
        model   = UserInfo
        exclude = ('user', 'posts', 'created', 'updated', 'comment')
        
        
    def clean_username(self):
        username = self.cleaned_data['username']
        try :
            User.objects.get(username=username)
        except User.DoesNotExist :
            return username
        raise forms.ValidationError("User name is already exists! Please use different name")
   
   
    def clean_password(self):
        password    = self.cleaned_data['password']
        password1   = self.cleaned_data['password1']
        if password != password1:
            raise forms.ValidationError("The password did not match please try again")
        return password
    
        
    
    
class LoginForm(forms.Form):
    username = forms.CharField(label=(u'User Name'), error_messages={'required' : 'User Name is required'})
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False), error_messages={'required' : 'Password is required'})
    
    
    
    
    
    
    