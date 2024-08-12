from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'
