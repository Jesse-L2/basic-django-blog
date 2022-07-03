from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView


# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # reverse_lazy allows importing when url is available
    template_name = 'registration/signup.html'

