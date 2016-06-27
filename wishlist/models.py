from django.contrib.auth.models import User
from django.db import models

class Wishlist(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
        
    
class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist)
    description = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    claimed = models.BooleanField(default=False)
    