from django.urls import path, include

from generator.views import index


app_name = "generator"

urlpatterns = [path("", index, name="index")]
