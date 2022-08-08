from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    birthday_year = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(unique=True)
