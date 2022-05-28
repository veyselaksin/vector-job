from django.shortcuts import render
from . import features_list

# Create your views here.
def index(requests):

    features = features_list.FEATURES_LIST

    context = {
        "hero_title": "Vector Job",
        "hero_text": "The job you've been looking for is here! If you are looking for a job, the vector job platform has been developed just for you. Don't wait, register now!",
        "features": features
    }
    return render(requests,"pages/index.html", context)

def home(requests):
    return render(requests, "pages/home.html")


def dashboard(requests):
    return render(requests, "pages/dashboard.html")