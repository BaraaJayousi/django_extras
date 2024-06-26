from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.


def index(request):
  createUserForm = UserCreateFrom()
  loginForm = UserLoginForm()
  context = {
    "registerForm": createUserForm,
    "loginForm": loginForm
  }

  return render(request, 'index.html', context)

def register(request):
  if request.method== 'POST':
    bound_user = UserCreateFrom(request.POST)
    if bound_user.is_valid():
      new_user = bound_user.save()
      login(request, new_user)
      return redirect('/success')
    
  return redirect('/')
  
def login_user(request):
  if request.method == 'POST':
    
    bound_user = UserLoginForm(request.POST)
    
    if bound_user.is_valid():
      authenticated_user = authenticate( username=request.POST['username'], password=request.POST['password'])
      if authenticated_user:
        login(request, authenticated_user)
        return redirect('/success')
  
  return redirect('/')

@login_required(login_url='/')
def login_success(request):
  return render(request, 'success.html')