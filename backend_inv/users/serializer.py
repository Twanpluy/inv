from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


# serializer to login
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(label="Username", max_length=255, write_only=True)
    password = serializers.CharField(
        label="Password", max_length=128, write_only=True, trim_whitespace=False
    )


# Serializer to Register a User
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    class Meta:
        model = User
        fields = ["username", "email", "password"]
        extra_kwargs = {"firstname": {"required": True}, "lastname": {"required": True}}

        # validata password = password2

        def val_password(self, attrs):
            if attrs["password"] != attrs["password2"]:
                raise serializers.ValidationError(
                    {"password": "Password fields didn't match"}
                )
            return attrs

        def create(self, validated_data):
            user = User.objects.create(
                username=validated_data["username"],
                email=validated_data["email"],
                firstname=validated_data["firstname"],
                lastname=validated_data["lastname"],
            )
            user.set_password(validated_data["password"])
            user.save()
            return user
