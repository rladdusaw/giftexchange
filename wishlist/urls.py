from django.conf.urls import url

from .views import WishlistView

urlpatterns = [
    url(r'create/$', WishlistView.as_view(), name='create_wishlist'),
]