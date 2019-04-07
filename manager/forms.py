from django import forms
from .models import *
import re
from django.contrib.auth.models import User
# from django import forms




class InternForm(forms.ModelForm):
    status=forms.CharField()
    
    
    class Meta:
        model = Intern
        fields="__all__"
        # exclude=('admin',)

    def __init__(self, *args, **kwargs):
        super(InternForm, self).__init__(*args, **kwargs)
        self.fields['admin'].initial=User.objects.filter(is_staff=True).exclude(is_superuser=False)[0]


    # def clean_phone(self):
    #     isbn = self.cleaned_data.get('phone', False)
    #     if Book.objects.filter(isbn=isbn).exists()==True or isbn==False:
    #         raise forms.ValidationError('The creation has failed')
    #     return isbn


class InternUpdateForm(forms.ModelForm):
    status=forms.CharField()
    class Meta:
        model = Intern
        exclude = ('phone','profilepic','document')

    def __init__(self, *args, **kwargs):
        super(InternUpdateForm, self).__init__(*args, **kwargs)
        self.fields['admin'].initial=User.objects.filter(is_staff=True).exclude(is_superuser=False)[0]


