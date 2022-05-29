from django.contrib import admin
from .models import ApplyJob, Job

# Register your models here.
admin.site.register(Job)
admin.site.register(ApplyJob)