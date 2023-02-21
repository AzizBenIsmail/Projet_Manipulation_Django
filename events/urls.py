from django.urls import path
from .views import *

urlpatterns = [
    path('homepage/<int:id>',HomePage,name='HomePage'),
    path('eventStatic/',eventStatic,name='event_Static'),
    path('listevent/',EventList,name='event_list'),
    path('EventListClass/',EventListClass.as_view(),name='Event_ListClass'),
    path('EventDetailClass/<int:pk>',EventDetailClass.as_view(),name='Event_DetailClass'),

]
