from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView

from braces.views import LoginRequiredMixin
from registration.backends.simple.views import RegistrationView

from wishlist.models import Wishlist

class HomeView(TemplateView):
    template_name = 'home.html'
    
class ProfileView(LoginRequiredMixin, ListView):
    model = Wishlist
    login_url = '/accounts/login/'
    template_name = 'wishlist_list.html'
    
    def get(self, request):
        owner = self.request.user
        return render(request, 'wishlist_list.html', {'owner': owner})

    
class CustomRegistrationView(RegistrationView):
    def get_success_url(self, request):
        return '/profile/'