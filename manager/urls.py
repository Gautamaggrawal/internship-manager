from django.urls import path,include
from manager.views import *
from django.contrib.auth.views import *
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required



urlpatterns = [

path('login/', LoginView.as_view(), name="login"),
    path('signup/',SignUpView.as_view(), name="signup"),
    path('', login_required(InternsListView.as_view(),login_url='login'), name="home"),
    path('interndetails/<int:pk>', login_required(InternDetailView.as_view(),login_url='login'), name='intern-detail'),
    path('interncreate/', login_required(InternCreateView.as_view(),login_url='login'), name='intern-create'),
    path('internupdate/<int:pk>', login_required(InternUpdateView.as_view(),login_url='login'), name='intern-update'),
    path('interndelete/<int:pk>', login_required(InternDeleteView.as_view(),login_url='login'), name='intern-delete'),
    path('accounts/logout/', LogoutView.as_view(template_name="manager/logout.html"), name='logout'),
    path('getresults/', Dynamic_Search, name='searches'),
]