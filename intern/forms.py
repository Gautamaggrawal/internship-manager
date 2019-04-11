from django import forms
from .models import *
import re
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, get_user_model,login



class InternSignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','password1')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active=False
        if commit:
            user.save()
        return user

# class CustomAuthenticationForm(forms.Form):
# 	username = forms.CharField(max_length=254)
# 	password = forms.CharField(label="Password", widget=forms.PasswordInput)
# 	def clean(self):
# 		username = self.cleaned_data.get('username')
# 		password = self.cleaned_data.get('password')
# 		print(username,password)
# 		if username and password:
# 			print(User.objects.filter(username=username))
# 			print(authenticate(username=username,password=password))	

# 			user_cache=User.objects.filter(username=username,password=password).exists()
# 			print(user_cache)
# 			if user_cache ==False:
# 				raise forms.ValidationError("incorrect cred")
# 			else:
# 				login(user_cache[0])
# 			# 	self.confirm_login_allowed(	user_cache)
# 		return self.cleaned_data
