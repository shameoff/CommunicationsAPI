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
    class Meta:
        model = Interlocutor
        fields = ('id', 'name', 'description')


class InterlocutorDetailSerializer(ModelSerializer):
    communications = serializers.SerializerMethodField()

    class Meta:
        model = Interlocutor
        fields = ["id", "name", "description", "communications", "owner"]
        read_only_fields = ["id", "communications", "owner"]

    def get_communications(self, obj):
        communications = obj.communication_set.all()
        # Сериализуем диалоги
        serializer = CommunicationsSerializer(communications, many=True)
        return serializer.data

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        print(validated_data['owner'])
        return Interlocutor.objects.create(**validated_data)
