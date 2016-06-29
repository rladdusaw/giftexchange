from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView

from wishlist.models import Wishlist

class HomeView(TemplateView):
    template_name = 'home.html'
    

