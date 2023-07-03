from django.urls import path

from user.views import SignUpView, UserLoginView

app_name = "user"

urlpatterns = [
    path("sign-up/", SignUpView.as_view(), name="sign-up"),
    path("login/", UserLoginView.as_view(), name="login"),
]
