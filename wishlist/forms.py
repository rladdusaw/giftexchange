from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Submit
from crispy_forms.bootstrap import FormActions

from .models import Wishlist, WishlistItem


class WishlistForm(ModelForm):
    class Meta:
        model = Wishlist
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(WishlistForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_wishlist_form'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = 'new_wishlist'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-4'
        self.helper.layout = Layout(
            Div(
                'name', 
                FormActions(
                Submit('submit', 'Submit')
                ),
                css_class='container col-md-6 col-md-offset-4'),
        )
        
        
        

class WishlistItemForm(ModelForm):
    class Meta:
        model = WishlistItem
        fields = ['description', 'link']