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
    class Meta:
        model = Interlocutor
        fields = ["name",
                  "description",
                  "user"]

    def create(self, validated_data):
        return Interlocutor.objects.create(**validated_data)
