from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from generator.forms import GeneratorForm


@login_required
def index(request):
    form = GeneratorForm()

    return render(request, template_name="index.html", context={"form": form})
