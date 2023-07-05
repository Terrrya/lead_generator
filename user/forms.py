from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.forms import (
    UserCreationForm as DefaultCreationForm,
    AuthenticationForm,
)
from django import forms

from user.models import User


class UserCreationForm(DefaultCreationForm):
    email = forms.EmailField(
        label="Email address", required=True, max_length=255
    )

    class Meta:
        model = User
        fields = DefaultCreationForm.Meta.fields + ("email",)

    helper = FormHelper()
    helper.form_class = "form-horizontal shadow bg-white"
    helper.label_class = "col-lg-2"
    helper.field_class = "col-lg-10"
    helper.layout = Layout(
        "username",
        "email",
        "password1",
        "password2",
        Submit("submit", "Submit", css_class="btn btn-primary"),
    )


class UserAuthenticationForm(AuthenticationForm):
    helper = FormHelper()
    helper.form_class = "form-horizontal shadow bg-white"
    helper.label_class = "col-lg-1"
    helper.field_class = "col-lg-11"
    helper.layout = Layout(
        "username",
        "password",
        Submit("submit", "Submit", css_class="btn btn-primary"),
    )
