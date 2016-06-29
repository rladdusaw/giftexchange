from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views as account_views

urlpatterns = [
	url(
		r'^login/$',
		auth_views.login,
		{'template_name': 'login.html'},
		name='login_view'
	),
	url(r'^logout/$', account_views.LogoutView.as_view(), name='logout_view'),
	url(r'^register/$', account_views.RegisterView.as_view(), name='register_view'),
	url(r'^error/$', account_views.ErrorView.as_view(), name='error_view'),
    url(r'^profile/$', account_views.ProfileView.as_view(), name='profile_view'),
]