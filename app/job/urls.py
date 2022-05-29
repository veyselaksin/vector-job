from django.urls import path
from . import views

urlpatterns = [
    path('jobs/<int:jobId>', views.job_details, name="job_details"),
    path('dashboard/jobs/add_job', views.add_job, name="add_job"),
    path('apply_job/<int:jobId>', views.apply_job, name="apply_job"),
    path('application/<int:applyId>', views.view_apply, name="view_apply") 
]