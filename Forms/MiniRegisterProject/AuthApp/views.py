from django.shortcuts import render, redirect
from .forms import *
from .models import User

# Create your views here.
def authentication(request):
  if request.method == 'POST':
    context ={}
    if request.POST['action'] == "Register":
      bound_form = RegistrationForm(request.POST)
      if bound_form.is_valid():
        new_user = bound_form.save()
        context = {
          "user": new_user
        }
      else:
        context ={
          "registration_form": bound_form
        }
        return render(request, 'auth.html', context)
    elif request.POST['action'] == "Login":
      bound_form = LoginForm(request.POST)
      print(bound_form.is_valid())
      print(bound_form.errors)
      if bound_form.is_valid():
        print("is valid login")
        context={
          "user": User.objects.filter(email=request.POST['email']).first()
        }
      else:
        context={
          "login_form": bound_form
        }
        return render(request, 'auth.html', context)
      
    return render(request, "success.html", context)
  else:
    registration_form = RegistrationForm()
    login_form = LoginForm()
    context = {
      "registration_form" : registration_form,
      "login_form": login_form
    }
  return render(request, 'auth.html', context)