from django.contrib.auth import get_user_model

from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            nickname = validated_data['nickname'],
            password = validated_data['password']
        )

        return user

    class Meta:
        model = get_user_model()
        fields = ['email', 'nickname', 'password']