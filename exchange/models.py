from django.contrib.auth.models import User
from django.db import models


class Exchange(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User)
    
    
class Participants(models.Model):
    participant = models.ForeignKey(User)
    exchange = models.ForeignKey(Exchange, related_name='participants')