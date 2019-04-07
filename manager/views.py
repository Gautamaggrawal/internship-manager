from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render, redirect,HttpResponse
from django.views.generic.edit import FormView
from django.views.generic import *
from .models import *
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import *
from django.db.models import Q

class SignUpView(FormView):
    form_class = UserCreationForm
    template_name = 'manager/signup.html'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return redirect('/')

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'manager/login.html'
    success_url=''


class InternCreateView(CreateView):
    form_class=InternForm
    template_name = 'manager/intern_form.html'
    success_message = "The intern created successfully"
    def form_valid(self,form):
        form.save()
        return redirect('/')

class InternUpdateView(SuccessMessageMixin,UpdateView):
    model=Intern
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
    form_class = InternUpdateForm
    success_url = '/'
    success_message = "The intern updated successfully"

class InternsListView(ListView):
	queryset = Intern.objects.all().order_by('-date_of_join')
	context_object_name = 'interns'

class InternDetailView(DetailView):
    model=Intern
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
    queryset = Intern.objects.filter()
    context_object_name = 'interns'

class InternDeleteView(SuccessMessageMixin,DeleteView):
    model=Intern
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
    success_message = "The Intern deleted successfully "
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(InternDeleteView, self).delete(request, *args, **kwargs)



def Dynamic_Search(request):

    if request.method == "GET":
        search_text = request.GET['search_text']
        if search_text is not None and search_text != u"":
            search_text = request.GET['search_text']
            statuss = Intern.objects.filter(Q(fullname__contains = search_text)|Q(email__contains=search_text))
        else:
            statuss = []

        return render(request, 'manager/intern_list.html', {'statuss':statuss})


