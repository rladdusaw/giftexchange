# /exchange/forms.py

from django.forms import ModelForm

from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Submit

from .models import Exchange, Participants


class ExchangeForm(ModelForm):
    class Meta:
        model = Exchange
        fields = ['name']
        
    def __init__(self, *args, **kwargs):
        super(ExchangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_exchange_form'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = '/exchange/create/'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-4'
        self.helper.layout = Layout(
            Div(
                'name',
                FormActions(
                    Submit('submit', 'Create')
                ),
                css_class = 'container col-md-6 col-md-offset-4'
            ),
        )