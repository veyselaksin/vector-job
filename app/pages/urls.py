from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('dashboard', views.dashboard, name="dashboard"),
    path('settings', views.settings, name="settings"),
    path('settings/profile', views.profile, name="profile"),
    path('settings/applied_jobs', views.applied_jobs, name="applied_jobs"),
    path('dashboard/<int:jobId>/applicants', views.view_applicants, name="view_applicants"),
    path('dashboard/applicant/<int:applicantId>', views.view_applicant, name="view_applicant")
]