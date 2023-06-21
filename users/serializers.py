from djoser.serializers import User
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'is_staff']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        read_only_fields = ['id', 'is_staff']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user
