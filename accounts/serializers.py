import re

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import CustomUser, Role


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        error_messages={
            "blank": "Email cannot be empty.",
        },
        validators=[
            UniqueValidator(
                queryset=CustomUser.objects.all(),
                message="This email is already registered.",
            )
        ],
    )
    phone = serializers.CharField(
        error_messages={
            "blank": "Phone cannot be empty.",
        },
        validators=[
            UniqueValidator(
                queryset=CustomUser.objects.all(),
                message="This phone is already registered.",
            )
        ],
    )
    password = serializers.CharField(
        error_messages={
            "blank": "Password cannot be empty.",
        },
    )

    class Meta:
        model = CustomUser
        fields = ["email", "phone", "password"]

    def validate_email(self, value):
        if not value.endswith("@example.com"):
            raise serializers.ValidationError("Email must be from example.com domain.")
        return value

    def validate_phone(self, value):
        if not re.match(r"^\d{11}$", value):
            raise serializers.ValidationError("Phone must be 11 digits.")
        return value

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError(
                "Password must be at least 6 characters long."
            )
        if not re.search(r"[A-Z]", value):
            raise serializers.ValidationError(
                "Password must contain at least one uppercase letter."
            )
        if not re.search(r"[0-9]", value):
            raise serializers.ValidationError(
                "Password must contain at least one digit."
            )
        return value

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data["phone"],
            phone=validated_data["phone"],
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        try:
            default_role = Role.objects.get(code="User")
        except Role.DoesNotExist:
            default_role = None
        user.role = default_role
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(
        error_messages={
            "blank": "Phone cannot be empty.",
        },
    )
    password = serializers.CharField(
        error_messages={
            "blank": "Password cannot be empty.",
        },
    )

    class Meta:
        model = CustomUser
        fields = ["phone", "password"]

    def validate_phone(self, value):
        if not re.match(r"^\d{11}$", value):
            raise serializers.ValidationError("Phone must be 11 digits.")
        return value

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError(
                "Password must be at least 6 characters long."
            )
        if not re.search(r"[A-Z]", value):
            raise serializers.ValidationError(
                "Password must contain at least one uppercase letter."
            )
        if not re.search(r"[0-9]", value):
            raise serializers.ValidationError(
                "Password must contain at least one digit."
            )
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email"]
