from django.shortcuts import render
from . import features_list
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from job.models import Job

# Create your views here.

def index(request):

    features = features_list.FEATURES_LIST

    context = {
        "hero_title": "Vector Job",
        "hero_text": "The job you've been looking for is here! If you are looking for a job, the vector job platform has been developed just for you. Don't wait, register now!",
        "features": features
    }
    return render(request,"pages/index.html", context)


@login_required(login_url="login_page")
def home(request):
    jobs = Job.objects.all()
    tags = Job.objects.annotate(tcount=Count('job_tag'))

    context = {
        "jobs": jobs,
        "tags": tags
    }
    return render(request, "pages/home.html", context)


@login_required(login_url="login_page")
def dashboard(request):
    return render(request, "pages/dashboard.html")