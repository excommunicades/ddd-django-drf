from rest_framework import serializers
from auths.domain.entities import UserEntity

from auths.domain.services import UserService


class UserRegistrationSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)

    def create(self, validated_data):

        user_entity = UserService.register_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        return user_entity

class UserLoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
