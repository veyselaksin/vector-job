from django.shortcuts import render
from . import features_list
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(requests):

    features = features_list.FEATURES_LIST

    context = {
        "hero_title": "Vector Job",
        "hero_text": "The job you've been looking for is here! If you are looking for a job, the vector job platform has been developed just for you. Don't wait, register now!",
        "features": features
    }
    return render(requests,"pages/index.html", context)


@login_required(login_url="login_page")
def home(requests):
    return render(requests, "pages/home.html")


@login_required(login_url="login_page")
def dashboard(requests):
    return render(requests, "pages/dashboard.html")