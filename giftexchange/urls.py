# /giftexchange/urls.py

from django.conf.urls import include, url
from django.contrib import admin

from registration.backends.simple import urls as registrtation_urls

from exchange import urls as exchange_urls
from wishlist import urls as wishlist_urls

from . import views as home_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', home_views.HomeView.as_view(), name='home'),
    url(
        r'^accounts/register/$',
        home_views.CustomRegistrationView.as_view(),
        name='registration_register'
    ),
	url(r'^accounts/', include(registrtation_urls)),
    url(r'^wishlist/', include(wishlist_urls)),
    url(r'^profile/$', home_views.ProfileView.as_view(), name='profile'),
    url(r'^exchange/', include(exchange_urls)),
]
