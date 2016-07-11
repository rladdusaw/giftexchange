from django.shortcuts import render
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, FormView

from braces.views import LoginRequiredMixin

from .forms import ExchangeForm

class ExchangeCreateView(LoginRequiredMixin, FormView):
    template_name = 'create_exchange.html'
    form_class = ExchangeForm
    

class ExchangeDetailView(LoginRequiredMixin, CreateView, SingleObjectMixin):
    template_name = 'exchange_detail.html'