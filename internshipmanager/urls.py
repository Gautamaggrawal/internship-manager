"""internshipmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from manager.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import *
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [

    path('admin/', admin.site.urls,name="yo"),
    path('login/', LoginView.as_view(), name="login"),
    path('signup/',SignUpView.as_view(), name="signup"),
    path('', staff_member_required(InternsListView.as_view(),login_url='login'), name="home"),
    path('intern/<int:pk>', staff_member_required(InternDetailView.as_view(),login_url='login'), name='intern-detail'),
    path('accounts/logout/', LogoutView.as_view(template_name="manager/logout.html"), name='logout'),

]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)