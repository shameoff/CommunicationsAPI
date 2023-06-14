from rest_framework import serializers

from communications.models import Communication


class CommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication
        fields = '__all__'