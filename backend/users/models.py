from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token

# Create your models here.

class MyUser(AbstractUser):
    username = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    birthday_year = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email



