from django.contrib.admin.models import LogEntry
from django.contrib import admin
from .models import *
admin.site.register(LogEntry)
admin.site.register(Intern)
