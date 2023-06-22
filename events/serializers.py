from rest_framework import serializers

from communications.serializers import CommunicationsSerializer
from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    communications = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ["id", "title", "image_id", "image_url", "description", "rating", "communications", "date"]

    def get_image_url(self, obj):
        pass

    def get_communications(self, obj) -> list:
        communications = obj.communication_set.all()
        # Сериализуем диалоги
        serializer = CommunicationsSerializer(communications, many=True)
        return serializer.data

