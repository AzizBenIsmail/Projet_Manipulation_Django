from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Person(AbstractUser):
    cin=models.CharField(primary_key=True,max_length=255)
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=25,unique=True)
    USERNAME_FIELD="username"