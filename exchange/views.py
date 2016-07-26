# /exchange/views.py

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, FormView

from braces.views import LoginRequiredMixin

from .forms import ExchangeForm
from .models import Exchange

class ExchangeCreateView(LoginRequiredMixin, FormView):
    template_name = 'create_exchange.html'
    form_class = ExchangeForm
    success_url = '/exchange/'
    login_url = '/accounts/login/'
    
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        exchange_list = Exchange.objects.filter(owner=user)
        form = self.form_class
        return render(
            request,
            'create_exchange.html',
            {'form': form, 'exchange_list': exchange_list}
        )
        
    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        exchange_list = Exchange.objects.filter(owner=user)
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        exchange = form.save(commit=False)
        exchange.owner = self.request.user
        exchange.save()
        return HttpResponseRedirect(self.get_success_url())
    
        
    
class ExchangeDetailView(LoginRequiredMixin, CreateView, SingleObjectMixin):
    template_name = 'exchange_detail.html'
    model = Exchange
    form_class = ExchangeForm
    login_url = '/accounts/login/'
    
    
        