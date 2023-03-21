from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Account(AbstractUser):
    semester = models.IntegerField(null=True,blank=True)
    phone_number = PhoneNumberField(blank=True)
    
    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.username