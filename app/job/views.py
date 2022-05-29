from django.shortcuts import render, redirect, get_object_or_404
from .models import ApplyJob, Job
from .forms import AddJobForm, ApplyJobForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login_page")
def job_details(request, jobId):
    job = Job.objects.get(pk=jobId)

    context = {
        "job": job,
        "user_type": request.user.usertype
    }

    return render(request, "job/job_details.html", context)

@login_required(login_url="login_page")
def apply_job(request, jobId):
    job = Job.objects.get(pk=jobId)
    form = ApplyJobForm()

    if request.method == "POST":
        form = ApplyJobForm(request.POST)

        if form.is_valid():
            apply = form.save(commit=False)
            apply.job = job
            apply.created_by = request.user
            apply.save()

            return redirect('home')
    
    context = {
        "form": form,
        "job": job
    }

    return render(request, "job/apply_job.html", context)

@login_required(login_url="login_page")
def add_job(request):
    form = AddJobForm()
    if request.method == 'POST':
        form = AddJobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()

            return redirect('dashboard')

    context = {
        "user_type": request.user.usertype,
        "form":form
    }

    return render(request, 'job/add_job.html', context)

@login_required(login_url="login_url")
def view_apply(request, applyId):
    apply = get_object_or_404(ApplyJob, pk=applyId, created_by=request.user)
    context = {
        "apply": apply
    }

    return render(request, "job/apply_details.html", context)