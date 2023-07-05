from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from user.forms import UserCreationForm, UserAuthenticationForm


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class UserLoginView(LoginView):
    form_class = UserAuthenticationForm
