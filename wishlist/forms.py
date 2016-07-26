# /wishlist/forms.py

from django.forms import ModelForm

from crispy_forms.bootstrap import FormActions, InlineField, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Layout, Submit

from .models import Wishlist, WishlistItem


class WishlistForm(ModelForm):
    """Uses crispy forms helper to format the wishlist creation form"""
    class Meta:
        model = Wishlist
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(WishlistForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_wishlist_form'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = '/wishlist/create/'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-4'
        self.helper.layout = Layout(
            Div(
                'name', 
                FormActions(
                    Submit('submit', 'Create')
                ),
                css_class='container col-md-6 col-md-offset-4'
            ),
        )
        
        
        

class WishlistItemForm(ModelForm):
    """Uses crispy forms helper to format the item creation form"""
    class Meta:
        model = WishlistItem
        fields = ['description', 'link']
        
    def __init__(self, current_list=None, *args, **kwargs):
        super(WishlistItemForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_wishlist_item_form'
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'
        self.helper.form_action = '.'
        self.helper.layout = Layout(
            Div(
                Field('description', placeholder='Description'),
                Field('link', placeholder='Link to item'),
                StrictButton('Add', value='submit', type='submit', css_class='btn-default'),
                css_class='container col-md-6 col-md-offset-4'
            ),
        )