from django.shortcuts import render
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model


# Create your views here.

class UsersViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.Serializer
