from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, TemplateView, View
from django.views.generic.edit import FormView

from wishlist.models import Wishlist


class LoggedInMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            redirect('login.html')
        return super(LoggedInMixin, self).dispatch(request, *args, **kwargs)

class ErrorView(TemplateView):
    template_name = 'error.html'


class LogoutView(View):
	
    def get(self,request):
        logout(request)
        return redirect('home')

class RegisterView(FormView):

    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = 'accounts/login/'

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)
        
class ProfileView(LoggedInMixin, ListView):
    template_name = 'profile.html'
    context_object_name = 'wishlists'
    
    def get_queryset(self):
        return Wishlist.objects.filter(owner=self.request.user)