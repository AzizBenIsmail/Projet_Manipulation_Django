from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import *
from django.core.exceptions import ValidationError
# Create your models here.
def ValidMail(value):
    if not str(value).endswith('@esprit.tn'):
        raise ValidationError("mail must ends with esprit.tn")
    return value
def lenValid(value):
    if len(value)!=8:
        raise ValidationError("verifier le nbr ")
    return value
class Person(AbstractUser):
    cin=models.CharField(primary_key=True,max_length=255,validators=[MinLengthValidator(limit_value=8,message='la valeur minimale doit etre 8 char'),
                                                                     MaxLengthValidator(limit_value=8,message="la valeur doit etre 8char")])
    email=models.EmailField(unique=True,validators=[ValidMail])
    username=models.CharField(max_length=25,unique=True)
    USERNAME_FIELD="username"
    
    def __str__(self) :
        return self.username