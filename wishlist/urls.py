# /wishlist/urls.py

from django.conf.urls import url

from .views import WishlistCreateView, WishlistDetailView

urlpatterns = [
    url(r'create/$', WishlistCreateView.as_view(), name='create_wishlist'),
    url(
        r'detail/(?P<current_list>[0-9]+)/$',
        WishlistDetailView.as_view(),
        name='wishlist_detail'
    ),
]