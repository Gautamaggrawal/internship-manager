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
    path('interndetails/<int:pk>', staff_member_required(InternDetailView.as_view(),login_url='login'), name='intern-detail'),
    path('interncreate/', staff_member_required(InternCreateView.as_view(),login_url='login'), name='intern-create'),
    path('internupdate/<int:pk>', staff_member_required(InternUpdateView.as_view(),login_url='login'), name='intern-update'),
    path('interndelete/<int:pk>', staff_member_required(InternDeleteView.as_view(),login_url='login'), name='intern-delete'),
    path('accounts/logout/', LogoutView.as_view(template_name="manager/logout.html"), name='logout'),

]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)