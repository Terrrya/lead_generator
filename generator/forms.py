from crispy_forms.helper import FormHelper
from django import forms


class GeneratorForm(forms.Form):
    keywords = forms.CharField(
        label="Keywords:",
        max_length=255,
        required=True,
    )
    location = forms.CharField(
        label="Location:",
        max_length=50,
        required=True,
    )
    leads_num = forms.ChoiceField(
        label="Lead num:",
        choices=list(zip(range(51), range(51))),
        required=True,
        initial=50,
    )
    helper = FormHelper()
    helper.form_class = "form-horizontal"
    helper.label_class = "col-lg-1"
    helper.field_class = "col-lg-11 shadow bg-white rounded p-0 m-0"
