from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from django.views.generic import ListView
# Create your views here.
def HomePage(req,id):
    response='hrllo from %s'
    return HttpResponse(response %id)
def eventStatic(req):
    list=[
        {
            'title':'title1',
            'description':'description'
        },
        {
            'title':'title2',
            'description':'description2'
        }
    ]
    return render(req,'events/StaticList.html',{'events':list})

def EventList(request):
    List=Event.objects.all()
    return render(request,'events/EventsList.html',{'events':List})

class EventListClass(ListView):
    model=Event
    template_name='events\EvenetListView.html'
    context_object_name='events'