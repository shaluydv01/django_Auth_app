from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .models import CustomUser
from .forms import CustomUserCreationForm  # Import the custom form

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # ✅ Use custom form
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/signup.html', {'form': form, 'login_url': reverse('login')})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form, 'signup_url': reverse('signup'), 'forgot_password_url': reverse('password_reset')})

@login_required
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html', {'username': request.user.username, 'profile_url': reverse('profile'), 'change_password_url': reverse('change_password'), 'logout_url': reverse('logout')})

@login_required
def profile_view(request):
    return render(request, 'auth/profile.html', {
        'username': request.user.username,
        'email': request.user.email,
        'date_joined': request.user.date_joined,
        'last_login': request.user.last_login,
        'dashboard_url': reverse('dashboard'),
        'logout_url': reverse('logout')
    })

def logout_view(request):
    logout(request)
    return redirect('login')

def password_reset_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                email_template_name='auth/password_reset_email.html',
                from_email=settings.DEFAULT_FROM_EMAIL
            )
            return redirect('login')  # Redirect user after submitting
    else:
        form = PasswordResetForm()
    return render(request, 'auth/password_reset.html', {'form': form})

@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            logout(request)
            return redirect('login')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'auth/change_password.html', {'form': form, 'dashboard_url': reverse('dashboard')})
