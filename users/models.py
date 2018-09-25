from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    # name = models.CharField(blank=True, max_length=100)
    username = models.CharField(max_length=40, unique=False, default='')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    house_phone = models.CharField(max_length=50, blank=True)
    cell_phone = models.CharField(max_length=50, blank=True)
    postal_address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    province = models.CharField(max_length=100, blank=True)
    pays = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.email