from django.db import models
from users.models import *
from datetime import date
from django.core.validators import *
from django.core.validators import MinValueValidator
from django.utils.timezone import datetime

# Create your models here.
def isDateValid(value):
    if value <= date.today():
        raise ValidationError('invalide date')
    return value
def istitleValid(value):
    if not value[0].isupper():  #isloweer
        raise ValidationError('invalide tite')
    return value
class Event(models.Model):
    category=(('musique','musique'),('cinema','cinema'),('sport','sport'))
    title=models.CharField(max_length=255,validators=[istitleValid])
    description=models.TextField()
    image=models.ImageField(upload_to='images/')
    categorie=models.CharField(max_length=8,choices=category)
    state=models.BooleanField(default=False)
    nbrParticipants=models.IntegerField(default=0,validators=[MinValueValidator(limit_value=0,message='le nbr de participon doit etre positive')])
    dateEvent=models.DateField(validators=[isDateValid]) 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    #association
    organizer =models.ForeignKey(Person,on_delete=models.CASCADE)
    participations=models.ManyToManyField(Person,related_name="Participation",through="Participation") #association ManyToMany
    #related_name-> esm l object
    def __str__(self) :
        return f'{self.title} and {self.state}'  #personalisation des interface
    class Meta:
        constraints=[models.CheckConstraint(check=models.Q(dateEvent__gte=datetime.now()),
                                            name="la date et invalide")]

#class intermediare
class Participation(models.Model):
    participationdate=models.DateTimeField(auto_now=True)
    personne=models.ForeignKey(Person,on_delete=models.CASCADE)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    class Meta:
        unique_together=('personne','event')