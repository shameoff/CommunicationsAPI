from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework.viewsets import ModelViewSet

from communications.models import Communication, Interlocutor
from communications.serializers import InterlocutorSerializer, CommunicationsSerializer


# Create your views here.

class CommunicationsViewSet(ModelViewSet):
    queryset = Communication.objects.all()
    serializer_class = CommunicationsSerializer


class InterlocutorViewSet(ModelViewSet):
    queryset = Interlocutor.objects.all()
    serializer_class = InterlocutorSerializer
