from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64, unique=True)
    phone = models.CharField(max_length=18, unique=True)
    discount_card_number = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=False)


class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
