from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, View
from django.views.generic.edit import FormView


class ErrorView(TemplateView):
    template_name = 'error.html'


class LogoutView(View):
	
    def get(self,request):
        logout(request)
        return redirect('home_view')

class RegisterView(FormView):

    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = '/error/'

    def form_valid(self, form):
        user = form.save()
        return redirect('login_view')