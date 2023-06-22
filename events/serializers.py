from rest_framework import serializers

from communications.serializers import CommunicationsSerializer
from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    communications = CommunicationsSerializer(read_only=True, many=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ["id", "title", "image_id", "image_url", "description", "rate", "communications", "date"]
        read_only_fields = ["id", "image_url"]

    def get_image_url(self, obj) -> str:
        return f"https://HOSTNAMEHERE/{obj.image_id}"

    def get_communications(self, obj) -> list:
        communications = obj.communication_set.all()
        # Сериализуем диалоги
        serializer = CommunicationsSerializer(communications, many=True)
        return serializer.data

