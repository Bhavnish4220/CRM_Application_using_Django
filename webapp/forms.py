from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record
from django.forms.widgets import PasswordInput,TextInput

# creating user

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']

# login user

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())

#create record

class CreateRecordForm(forms.ModelForm):
    class Meta:
        model=Record
        fields=['first_name','last_name','email','phone','address','city','province','country']

#update record

class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model=Record
        fields=['first_name','last_name','email','phone','address','city','province','country']