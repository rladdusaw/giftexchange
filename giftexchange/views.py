from django.template.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView

from crispy_forms.utils import render_crispy_form
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
        
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        ctx = {}
        ctx.update(csrf(request))
        form_html = render_crispy_form(form, context=ctx)
        if form.is_valid():
            return self.form_valid(form)
        else:
            ctx['form_errors'] = form.errors
            return self.render_to_response(
                self.get_context_data(form=form, form_html=form_html)
            )