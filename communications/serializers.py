from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from communications.models import Communication, Interlocutor


class CommunicationsSerializer(ModelSerializer):
    class Meta:
        model = Communication
        fields = ["name",
                  "description",
                  "date",
                  "rate",
                  "interlocutor"]

    def create(self, validated_data):
        return Communication.objects.create(**validated_data)


class InterlocutorSerializer(ModelSerializer):
    # owner = serializers.Related(
    #     read_only=True,
    #     default=serializers.CurrentUserDefault()
    # )

    class Meta:
        model = Interlocutor
        fields = ["name",
                  "description",
                  "owner"]
        read_only_fields = ["owner"]

    def create(self, validated_data):
        print(f"ЭТО АВТООРИЗОВАННЫЙ ПОЛЬЗОВАТЕЛЬ {serializers.CurrentUserDefault()}")
        validated_data['owner'] = self.context['request'].user
        return Interlocutor.objects.create(**validated_data)
