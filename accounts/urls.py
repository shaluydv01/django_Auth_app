from django.contrib.auth import views as auth_views
from django.urls import path
from accounts.views import password_reset_view
from .views import signup_view, login_view, dashboard_view, profile_view, logout_view, password_reset_view, change_password_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('password-reset/', password_reset_view, name='password_reset'),
    path('change-password/', change_password_view, name='change_password'),
    # Built-in Django views for password reset
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="auth/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="auth/password_reset_complete.html"), name='password_reset_complete'),
]
