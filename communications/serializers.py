from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from communications.models import Communication, Interlocutor


class CommunicationsSerializer(ModelSerializer):
    class Meta:
        model = Communication
        fields = ["id", "name", "description", "date", "rate", "interlocutor"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        return Communication.objects.create(**validated_data)


class InterlocutorSerializer(ModelSerializer):
    class Meta:
        model = Interlocutor
        fields = ["id", "name", "description", "owner"]
        read_only_fields = ["owner", "id"]

    def create(self, validated_data):
        print(f"ЭТО АВТООРИЗОВАННЫЙ ПОЛЬЗОВАТЕЛЬ {serializers.CurrentUserDefault()}")
        validated_data['owner'] = self.context['request'].user
        return Interlocutor.objects.create(**validated_data)
