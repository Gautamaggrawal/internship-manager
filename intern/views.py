from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect,HttpResponse
from django.views.generic.edit import FormView
from django.views.generic import *
from .models import *
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import *    
from django.db.models import Q
from django.views.generic import View
from django.contrib.auth.hashers import check_password


class InternSignUpView(View):
    template_name='registration/internlogin.html'

    def post(self, request):
        username=request.POST.get("username")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")
        if User.objects.filter(username=username).exists():
            return render(request, self.template_name, {'error': "user already exists"})
        if password1==password2:
            user = User.objects.create_user(username=username,password=password1)
            user.is_active=False
            user.save()
            print(user)
            login(request,user)
            return redirect('/internhome/')

class InternLoginView(View):
    template_name='registration/internlogin.html'

    def post(self, request):
        print(request.POST)
        username=request.POST.get("username")
        password=request.POST.get("password")
        if User.objects.filter(username=username).exists()==False:
            return render(request, self.template_name, {'error': "User does not exists"})
        elif User.objects.filter(username=username).exists():
            if User.objects.get(username=username).is_active==False:
                user=User.objects.get(username=username)
                if check_password(password, user.password):
                    login(request,user)
                    return redirect('/internhome/')    
                else:
                    return render(request, self.template_name, {'error': "Incorrect password"})
            else:
                return render(request, self.template_name, {'error': "Incorrect credentials"})







# class InternSignUpView(FormView):
#     form_class = InternSignUpForm
#     template_name = 'manager/signup.html'

#     def form_valid(self, form):
#         form.save()
#         username = form.cleaned_data.get('username')
#         raw_password = form.cleaned_data.get('password1')
#         user = authenticate(username=username, password=raw_password)
#         login(self.request, user)
#         return redirect('/internhome/')

# class InternLoginView(FormView):
#     form_class = AuthenticationForm
#     template_name = 'registration/login.html'
#     success_url='/internhome/'

#     def form_valid(self, form):
#         login(self.request, form.get_user())
#         return redirect('/internhome/')
