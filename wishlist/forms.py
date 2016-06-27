from django.forms import ModelForm

from .forms import Wishlist, WishlistItem


class WishlistForm(ModelForm):
    class Meta:
        model = Wishlist
        fields = ['name']
        

class WishlistItemForm(ModelForm):
    class Meta:
        model = WishlistItem
        fields = ['descritpion', 'link']