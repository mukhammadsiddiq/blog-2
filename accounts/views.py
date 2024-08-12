from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomUserCreation
from django.urls import reverse_lazy
# Create your views here.


class SignupView(CreateView):
    form_class = CustomUserCreation
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'