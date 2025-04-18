from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)
    
    class Meta:
        ordering = ['username']
    
    def __str__(self):
        return self.username