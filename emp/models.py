from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    DEFAULT_COMPANY_ID = 1

    id = models.AutoField(primary_key=True)
    employee_code = models.CharField(max_length=16, default=None, null=True)
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    mobile_no = models.CharField(max_length=10, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','username']

    def __str__(self):
        return(self.username)