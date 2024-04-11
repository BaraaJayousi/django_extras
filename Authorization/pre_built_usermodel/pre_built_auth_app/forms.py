from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreateFrom(UserCreationForm):
  email = forms.EmailField(required=True)
  first_name = forms.CharField(max_length=30, required= True)
  last_name = forms.CharField(max_length=30, required= True)
  class Meta:
    model= User
    fields = ['first_name', 'last_name','username', 'email','password1', 'password2']
    
    def save(self, commit=True):
      user= super(UserCreateFrom,self).save(commit=False)
      user.email = self.cleaned_data['email']
      user.first_name = self.cleaned_data['first_name']
      user.last_name = self.cleaned_data['last_name']
      if commit:
        user.save()
      return user
    

class UserLoginForm(forms.Form):
  username= forms.CharField(max_length=160, required=True)
  password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput)