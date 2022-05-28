from django.urls import path
from . import views

urlpatterns = [
    path('jobs/<int:jobId>', views.job_details, name="job_details")
]