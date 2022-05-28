from django.shortcuts import render, redirect
from .forms import CreateUserForm

# Create your views here.
def register(requests):
    form = CreateUserForm()

    if requests.method == "POST":
        form = CreateUserForm(requests.POST)
        if form.is_valid():
            print(requests.POST)
            form.save()
            return redirect("login")

    context = {
        "form": form
    }
    return render(requests, "users/register.html", context)

def login(requests):
    return render(requests, "users/login.html")

def logout(reqeuests):
    return render()