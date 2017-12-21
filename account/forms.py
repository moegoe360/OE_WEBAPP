from django.contrib.auth import get_user_model #imports current user model
from django.contrib.auth.forms import UserCreationForm

from django import forms
from .models import User
from .models import Profile
from django.forms import extras
from account.choices import YEARS_CHOICES
import datetime
from .choices import *
from django.forms.widgets import RadioSelect

#from .validators import validate_email_unique <- Do we even need?
class UserCreateForm(UserCreationForm):
    """
        The form used to create a user
    """
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class LoginForm(forms.Form):
    """
        The form used in the login screen
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
        
class UserEditForm(forms.ModelForm):
    """
        The form used to edit the user information
    """
    class Meta:
        model = User
        fields = ('email',)
          
class ProfileEditForm(forms.ModelForm):
    """
        The form used to edit participant pre-information
    """
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'age','gender', 'race', 'education')
        widgets = {
            'date_of_birth': extras.SelectDateWidget(
                empty_label=('Year', 'Month', 'Day'), 
                years=range(1920, datetime.datetime.now().year-8)),        
        } 
             
 #Used an Auth Form that handled all the checks

# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#     passwordRepeat = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#     
#     class Meta:
#         model = User
#         fields = ('username', 'email')
#         
#     def clean_password2(self):
#         pvc = self.cleaned_data
#         if pvc['password'] != pvc['passwordRepeat']:
#             raise forms.ValidationError('Passwords don\'t match.')
#         return pvc['passwordRepeat']
#     
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         username = self.cleaned_data.get('username')
#         if email and User.objects.filter(email=email).exclude(username=username).exists():
#             raise forms.ValidationError(u'That email address has already been used. Please use a different email.')
#         return email