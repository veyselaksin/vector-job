from django.shortcuts import render
from .models import Job

# Create your views here.
def job_details(request, jobId):
    job = Job.objects.get(pk=jobId)

    context = {
        "job": job
    }

    return render(request, "job/job_details.html", context)