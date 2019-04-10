from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect,HttpResponse
from django.views.generic.edit import FormView
from django.views.generic import *
from .models import *
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import *
from django.db.models import Q

class InternSignUpView(FormView):
    form_class = InternSignUpForm
    template_name = 'manager/signup.html'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return redirect('/internhome/')

class InternLoginView(FormView):
    form_class = CustomAuthenticationForm
    template_name = 'registration/login.html'
    success_url='/internhome/'


