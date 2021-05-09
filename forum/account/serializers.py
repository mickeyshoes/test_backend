from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken

class CreateAndModifyUserSerializer(serializers.Serializer):
    login_id = serializers.CharField(required=True, max_length=50)
    email = serializers.CharField(required=True, max_length=100)
    password = serializers.CharField(required=True)

    def create(self, validated_data):
        user = User.objects.create(
            login_id = validated_data['login_id'],
            email = validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

    def change_password(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return user


