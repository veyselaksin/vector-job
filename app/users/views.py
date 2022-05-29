from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.models import UserType
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .token import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
# Create your views here.


def register_page(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if User.objects.filter(email=request.POST.get('email')).exists():
            messages.warning(request, "This mail address already taken!")
        else:
            if form.is_valid():
                user = form.save()

                account_type = request.POST.get('accountType')

                if account_type == "manager_account":
                    usertype = UserType.objects.create(
                        user=user, is_manager=True)
                    usertype.save()
                else:
                    usertype = UserType.objects.create(
                        user=user, is_manager=False)
                    usertype.save()
                    
                current_site = get_current_site(request)
                mail_subject = 'Activation link has been sent to your email id'
                message = render_to_string('pages/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return render(request, 'pages/mail_template.html', {'msg': 'Please confirm your email address to complete the registration'})

    context = {
        "form": form
    }
    return render(request, "users/register.html", context)


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'pages/mail_template.html', {'msg': 'Thank you for your email confirmation. Now you can login your account.'})
    else:
        return render(request, 'pages/mail_template.html', {'msg': 'Activation link is invalid!'})


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Username or password is incorrect!')

    context = {}
    return render(request, "users/login.html", context)


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')
