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
    
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Your account has been created successfully. You can now log in.")
        return response
    
class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('dashboard')
    
    def get_success_url(self):
        return self.success_url
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request,'You have successfully logged in!')
        return response
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Invalid login credentials. Please try again.')
        return response
    
    
    
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')
    
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'You have been logged out!')
        return super().dispatch(request, *args, **kwargs)
