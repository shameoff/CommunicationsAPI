from django.shortcuts import render
from rest_framework import generics, serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from communications.models import Communication, Interlocutor
from communications.serializers import CommunicationsSerializer, InterlocutorListSerializer, \
    InterlocutorDetailSerializer


# Create your views here.

class CommunicationsViewSet(ModelViewSet):
    queryset = Communication.objects.all()
    serializer_class = CommunicationsSerializer

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


class InterlocutorViewSet(ModelViewSet):
    queryset = Interlocutor.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return InterlocutorListSerializer
        elif self.action == 'retrieve':
            return InterlocutorDetailSerializer
        return super().get_serializer_class()

