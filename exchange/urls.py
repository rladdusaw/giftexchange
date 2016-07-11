from django.conf.urls import url

from .views import ExchangeCreateView, ExchangeDetailView

urlpatterns = [
    url(r'^$', ExchangeCreateView.as_view(), name='create_exchange'),
    url(r'^create/$', ExchangeCreateView.as_view(), name='create_exchange'),
    url(r'^detail/$', ExchangeDetailView.as_view(), name='exchange_detail'),
]