from django.urls import path
from .views import *

urlpatterns = [
    path('homepage/<int:id>',HomePage,name='HomePage'),
    path('eventStatic/',eventStatic,name='event_Static'),
    path('hghhjb/',EventList,name='event_list'),
    path('create_event/',create_event,name='create_event'),
    path('EventListClass/',EventListClass.as_view(),name='Event_ListClass'),
    path('EventDetailClass/<int:pk>',EventDetailClass.as_view(),name='Event_DetailClass'),

]
