"""/giftexchange/urls.py"""

from django.conf.urls import include, url
from django.contrib import admin

from accounts import urls as account_urls

from . import views as home_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', home_views.HomeView.as_view(), name='home_view'),
	url(r'^accounts/', include(account_urls)),
]
