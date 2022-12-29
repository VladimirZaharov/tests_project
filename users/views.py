from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserLoginForm, UserRegistrationForm
from users.models import User


class LoginLoginView(LoginView):
    model = User
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('tests:index')


class RegistrationCreateView(CreateView):
    model = User
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('tests:index')


class LogoutLogoutView(LogoutView):
    next_page = 'index'
