from django.shortcuts import render
from rest_framework import generics, serializers, status, filters
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from communications.models import Communication, Interlocutor
from communications.serializers import CommunicationsSerializer, InterlocutorListSerializer, \
    InterlocutorDetailSerializer
from rest_framework.permissions import *


# Create your views here.
class CommunicationsOwnerFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        # Получение текущего пользователя
        user = request.user

        # Фильтрация коммуникаций по принадлежности собеседника пользователю
        filtered_queryset = queryset.filter(interlocutor__owner=user)

        return filtered_queryset


class CommunicationsViewSet(ModelViewSet):
    queryset = Communication.objects.all()
    serializer_class = CommunicationsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [CommunicationsOwnerFilterBackend]

    def perform_create(self, serializer):
        # Получение текущего пользователя
        user = self.request.user

        # Получение собеседника по указанному ID
        interlocutor_id = self.request.data.get('interlocutor')
        interlocutor = Interlocutor.objects.get(id=interlocutor_id)

        # Проверка на принадлежность собеседника пользователю
        if interlocutor.owner != user:
            return Response({'error': 'Собеседник не существует или не принадлежит пользователю'}, status=status.HTTP_400_BAD_REQUEST)

        # Создание беседы
        serializer.save()


class InterlocutorOwnerFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(owner=request.user)


class InterlocutorViewSet(ModelViewSet):
    queryset = Interlocutor.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [InterlocutorOwnerFilterBackend]

    def get_serializer_class(self):
        if self.action == 'list':
            return InterlocutorListSerializer
        return InterlocutorDetailSerializer
