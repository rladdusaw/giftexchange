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
    template_name = 'create_wishlist.html'
    form_class = WishlistForm
    success_url = '/profile/'
    
    def form_valid(self, form):
        wishlist = form.save(commit=False)
        wishlist.owner = self.request.user
        wishlist.save()
        return HttpResponseRedirect(self.get_success_url())
        
    
        
class WishlistDetailView(LoginRequiredMixin, CreateView, SingleObjectMixin):
    template_name = 'wishlist_detail.html'
    model = WishlistItem
    form_class = WishlistItemForm
    
    def get_form_kwargs(self):
        kwargs = super(WishlistDetailView, self).get_form_kwargs()
        kwargs.update(self.kwargs)
        return kwargs
        
    def get(self, request, current_list):
        wishlist = Wishlist.objects.get(id=current_list)
        wishlistitems = wishlist.wishlistitem_set.all()
        print(wishlistitems)
        form = self.form_class
        return render(request, 'wishlist_detail.html', {'form': form, 'wishlist': wishlist})
    
    def form_valid(self, form):
        wishlist_item = form.save(commit=False)
        wishlist_item.wishlist = Wishlist.objects.get(
            id=self.kwargs['current_list']
        )
        wishlist_item.save()
        return HttpResponseRedirect(
            '/wishlist/detail/%s/' % (self.kwargs['current_list'],)
        )