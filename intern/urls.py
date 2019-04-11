from django.urls import path,include
from intern.views import *
from django.contrib.auth.views import *
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import TemplateView


urlpatterns = [
	  path('signup/', InternSignUpView.as_view(), name="intern-signup"),
	  path('login/', InternLoginView.as_view(), name="intern-login"),
	  path('', TemplateView.as_view(template_name='registration/internlogin.html'))
]