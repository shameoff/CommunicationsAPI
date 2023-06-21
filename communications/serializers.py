from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from communications.models import Communication, Interlocutor


class CommunicationsSerializer(ModelSerializer):
    class Meta:
        model = Communication
        fields = ["id", "name", "description", "date", "rate"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        return Communication.objects.create(**validated_data)


class InterlocutorListSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField()

    class Meta:
        model = Interlocutor
        fields = ('id', 'name', 'description', 'rate', 'avatar_url')

    def get_avatar_url(self, obj):
        pass

    def get_rate(self, obj):
        communications = obj.communication_set.all()
        total_rate = sum(communication.rate for communication in communications)
        return total_rate


class InterlocutorDetailSerializer(ModelSerializer):
    communications = serializers.SerializerMethodField()
    rate = serializers.SerializerMethodField()

    class Meta:
        model = Interlocutor
        fields = ["id", "name", "description", "communications", "owner", 'rate', 'avatar_url', 'avatar_id']
        read_only_fields = ["id", "communications", "owner", 'rate']

    def get_avatar_url(self, obj):
        pass

    def get_communications(self, obj):
        communications = obj.communication_set.all()
        # Сериализуем диалоги
        serializer = CommunicationsSerializer(communications, many=True)
        return serializer.data

    def get_rate(self, obj):
        communications = obj.communication_set.all()
        total_rate = sum(communication.rate for communication in communications)
        return total_rate

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        print(validated_data['owner'])
        return Interlocutor.objects.create(**validated_data)
