from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.


class User(models.Model):
    username = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=8)

    def __str__(self):
        return self.username


class Contact(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=11,unique=True)

    def __str__(self):
        return self.contact
