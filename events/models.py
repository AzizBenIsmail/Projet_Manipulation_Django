from django.db import models
from users.models import *
from datetime import date
from django.core.validators import *

# Create your models here.
def isDateValid(value):
    if value <= date.today():
        raise ValueError('invalide date')
    return value

class Event(models.Model):
    category=(('musique','musique'),('cinema','cinema'),('sport','sport'))
    title=models.CharField(max_length=255)
    description=models.TextField()
    image=models.ImageField(upload_to='images/')
    categorie=models.CharField(max_length=8,choices=category)
    state=models.BooleanField(default=False)
    nbrParticipants=models.IntegerField(default=0)
    dateEvent=models.DateField(validators=[isDateValid])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    #association
    organizer =models.ForeignKey(Person,on_delete=models.CASCADE)
    participations=models.ManyToManyField(Person,related_name="Participation",through="Participation")
    #related_name-> esm l object

class Participation(models.Model):
    participationdate=models.DateTimeField(auto_now=True)
    personne=models.ForeignKey(Person,on_delete=models.CASCADE)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)