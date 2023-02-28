from django.urls import path
from .views import *

urlpatterns = [
    path('homepage/<int:id>',HomePage,name='HomePage'),
    path('eventStatic/',eventStatic,name='event_Static'),
    path('listevent/',EventList,name='event_list'),
    path('createEvent/',create_event,name='create_event'),
    path('add_event/',add_event,name='add_event'),
    path('CreateEventView/',CreateEvent.as_view(),name='create_event_view'),
    path('UpdateEventView/<int:pk>',ModelUpdateView.as_view(),name='update_event_view'),
    path('EventListClass/',EventListClass.as_view(),name='Event_ListClass'),
    path('EventDetailClass/<int:pk>',EventDetailClass.as_view(),name='Event_DetailClass'),

]
