from django.shortcuts import render
from rest_framework import generics

from events.models import Event
from events.serializers import EventSerializer


# Create your views here.

class EventAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
