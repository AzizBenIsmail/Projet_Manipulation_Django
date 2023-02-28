from django import forms
from .models import Event
from users.models import Person
class EventForm(forms.Form):
    title=forms.CharField(label='Title', max_length=9,
                               widget=forms.TextInput(attrs={
                                   'class':'form-control'}), required=False)
    description=forms.CharField(label='description', widget=forms.TextInput, required=False)
    image=forms.ImageField(label='Image', required=False)
    categorie=forms.ChoiceField(choices=Event.category,widget=forms.RadioSelect)
    nbrParticipants=forms.IntegerField(label='Participants',min_value=0,max_value=710)
    dateEvent=forms.DateField(
        label='Date Event', 
        widget=forms.DateInput(
        attrs={ 
               'type': 'date',
               }))
    organizer=forms.ModelChoiceField(label='Event Organizer',queryset=Person.objects.all())
    
class EventModelform(forms.ModelForm):
    
    class Meta:
        model = Event
        fields = ['title','description','categorie','image','organizer','dateEvent','nbrParticipants']
        exclude=('state',)
    dateEvent=forms.DateField(
        label="Event Date",
        widget=forms.DateInput(
        attrs={
        'type' : 'date',
        'class' :'form-control date-input'
        }
        ))
    organizer=forms.ModelChoiceField(label="Event Organizer",
        queryset=Person.objects.all())
