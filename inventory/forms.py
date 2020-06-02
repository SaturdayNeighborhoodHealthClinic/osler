from django import forms
from django.forms import ModelForm
from . import models

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import InlineCheckboxes
from crispy_forms.layout import ButtonHolder, Submit

from crispy_forms.layout import Field
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class DrugForm(ModelForm):
    class Meta:
        model = models.Drug
        fields = ['name', 'unit', 'dose', 'total_inventory', 'category']

    def __init__(self, *args, **kwargs):
        super(DrugForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', 'Submit'))
