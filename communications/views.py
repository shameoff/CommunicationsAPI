from django.shortcuts import render
from rest_framework import generics

from communications.models import Communication
from communications.serializers import CommunicationSerializer


# Create your views here.

class CommunicationAPIView(generics.ListAPIView):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer
