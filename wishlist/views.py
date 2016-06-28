from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import WishlistForm

class WishlistView(FormView):
    template_name = 'create_wishlist.html'
    form_class = WishlistForm
    success_url = '/profile/'