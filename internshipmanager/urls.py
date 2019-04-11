from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from django.views.generic import TemplateView

urlpatterns = [

    path('admin/', admin.site.urls,name="yo"),
    path('internmanager', include('manager.urls')),
    path('internstudent/', include('intern.urls')),
    path('', TemplateView.as_view(template_name='welcome.html'))
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)