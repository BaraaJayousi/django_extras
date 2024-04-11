from django import forms
from .models import User
from .validators import *

class RegistrationForm(forms.ModelForm):
  confirm_password = forms.CharField(max_length=100,widget=forms.PasswordInput)

  def clean_confirm_password(self):
    cleaned_data = super().clean()
    password = cleaned_data.get("password")
    confirm_password = cleaned_data.get("confirm_password")
    validate_password_match(password, confirm_password)

  def clean_password(self):
    data = self.cleaned_data['password']
    password_pattern_validator(data)
    return data

  def clean_email(self):
    data = self.cleaned_data['email']
    check_unique_email(User, data)
    return data
  
  class Meta:
    model = User
    fields = '__all__'
    widgets = {
      "password": forms.PasswordInput
    }


class LoginForm(forms.ModelForm):
  def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data.get("password")
    email = cleaned_data.get("email")
    validate_user_login(User, email, password)


  class Meta:
    model = User
    fields = ['email', 'password']
    widgets = {
      "password": forms.PasswordInput
    }