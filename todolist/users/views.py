from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
# Create your views here.

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')
    
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')