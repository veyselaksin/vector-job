from django.shortcuts import render, redirect
from . import features_list
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from users.forms import CreateUserForm
from job.models import ApplyJob, Job, job_tags
from django.contrib.auth.models import User

# Create your views here.


def index(request):

    features = features_list.FEATURES_LIST

    if request.user.is_authenticated:
        return redirect("home")

    context = {
        "hero_title": "Vector Job",
        "hero_text": "The job you've been looking for is here! If you are looking for a job, the vector job platform has been developed just for you. Don't wait, register now!",
        "features": features
    }
    return render(request, "pages/index.html", context)


@login_required(login_url="login_page")
def home(request):
    jobs = Job.objects.all()
    temp = Job.objects.none()

    if request.method == "POST":
        list_of_tags = request.POST.getlist("tags")

        for tag in list_of_tags:
            if tag == "all":
                jobs = Job.objects.all()
            else:
                jobs = Job.objects.filter(Q(title__icontains=tag) | Q(description__icontains=tag))
                temp = temp | jobs
                jobs = temp

    context = {
        "jobs": jobs,
        "tags": job_tags,
        "user_type": request.user.usertype
    }
    return render(request, "pages/home.html", context)


@login_required(login_url="login_page")
def dashboard(request):
    context = {
        "user_type": request.user.usertype,
        "jobs": request.user.jobs.all
    }
    return render(request, "pages/dashboard.html", context)


@login_required(login_url="login_page")
def settings(request):

    context = {
        "user_type": request.user.usertype,
        "user": request.user
    }
    return render(request, "pages/settings.html", context)


@login_required(login_url="login_page")
def profile(request):
    form = CreateUserForm(instance=request.user)

    if request.method == "POST":
        form = CreateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("home")
        
        print(form.errors)
    context = {
        "user_type": request.user.usertype,
        "user": request.user,
        "form": form
    }
    return render(request, "pages/profile.html", context)


@login_required(login_url="login_page")
def applied_jobs(request):

    context = {
        "user_type": request.user.usertype,
        "user": request.user,
        "applied_jobs": request.user.apply_job.all
    }
    return render(request, "pages/applied_jobs.html", context)


@login_required(login_url="login_page")
def view_applicants(request, jobId):
    applicants = ApplyJob.objects.all()
    job = Job.objects.get(pk=jobId)

    context = {
        "applicants": applicants,
        "job": job,
        "user_type": request.user.usertype
    }

    return render(request, "pages/applicants.html", context)


@login_required(login_url="login_page")
def view_applicant(request, applicantId):
    applicant = ApplyJob.objects.get(pk=applicantId)

    context = {
        "applicant": applicant,
        "user_type": request.user.usertype
    }

    return render(request, "pages/applicant_detail.html", context)
