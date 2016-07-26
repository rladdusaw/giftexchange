# /wishlist/views.py

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, FormView

from braces.views import LoginRequiredMixin

from .forms import WishlistForm, WishlistItemForm
from .models import Wishlist, WishlistItem

class WishlistCreateView(LoginRequiredMixin, FormView):
    """
    Uses the FormView class to display the wishlist creation form and the
    LoginRequiredMixin mixin to make sure the user is authenticated
    """
        
    template_name = 'create_wishlist.html'
    form_class = WishlistForm
    success_url = '/profile/'
    login_url = '/accounts/login/'
    
    def form_valid(self, form):
        """
        Overrides the form_valid method to automatically save the current user
        as the owner of the new wishlist.
        """
        
        wishlist = form.save(commit=False)
        wishlist.owner = self.request.user
        wishlist.save()
        return HttpResponseRedirect(self.get_success_url())
        
    
        
class WishlistDetailView(LoginRequiredMixin, CreateView, SingleObjectMixin):
    """
    Uses the CreateView class and the SingleObjectMixin mixin to create new
    wishlist items. Used the LoginRequiredMixin mixin to ensure the user is 
    authenticated.
    """
    
    template_name = 'wishlist_detail.html'
    model = WishlistItem
    form_class = WishlistItemForm
    login_url = '/accounts/login/'
    
        
    def get(self, request, current_list):
        """
        Overrides the get method to expose the form and wishlist items for
        the current wishlist.
        """
        
        wishlist = Wishlist.objects.get(id=current_list)
        wishlistitems = wishlist.wishlistitem_set.all()
        form = self.form_class
        return render(request, 'wishlist_detail.html', {'form': form, 'wishlist': wishlist})
    
    def form_valid(self, form):
        """
        Overrides the form_valid method to automatically attach the current
        wishlist to the new item.
        """
        
        wishlist_item = form.save(commit=False)
        wishlist_item.wishlist = Wishlist.objects.get(
            id=self.kwargs['current_list']
        )
        wishlist_item.save()
        return HttpResponseRedirect(
            '/wishlist/detail/%s/' % (self.kwargs['current_list'],)
        )
        