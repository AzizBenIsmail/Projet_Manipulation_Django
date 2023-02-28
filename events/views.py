from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Event
from django.views.generic import *
from .forms import EventForm,EventModelform
from django.urls import reverse_lazy
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
    List=Event.objects.filter(state=True)
    return render(request,'events/EventsList.html',{'events':List})

class EventListClass(ListView):
    model=Event
    template_name='events/EvenetListView.html'
    context_object_name='events'
        
    
class EventDetailClass(DetailView):
    model=Event
    template_name='events\EventDetailClass.html'
    context_object_name='event'
    
def create_event(request):
    form=EventForm()
    if request.method == 'POST':
        form=EventForm(request.POST, request.FILES)
        if form.is_valid():
            Event.objects.create(**form.cleaned_data)
            return redirect('Event_ListClass')
        else:
            print(form.errors)
    return render(request,'events/event_form.html',{'form':form})

def add_event(request):
    if request.method == 'GET':
        form = EventModelform()
        return render(request,'events/event_form.html',{'form':form})
    if request.method == 'POST':
        form=EventModelform(request.POST, request.FILES)
        if form.is_valid():
            Event=form.save(commit=False)
            Event.save()
            return redirect('Event_ListClass')
        else:
            return render(request,"events/event_form.html",{'form':form})

class CreateEvent(CreateView):   #best in Exam
    model = Event
    template_name = "events/event_form.html"
    form_class=EventModelform
    success_url = reverse_lazy('Event_ListClass')
    
class ModelUpdateView(UpdateView):
    model = Event
    template_name = "events/event_form.html"
    form_class=EventModelform
    success_url = reverse_lazy('Event_ListClass')
