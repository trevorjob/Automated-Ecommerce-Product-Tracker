from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User


class UserRegisterserializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "email"]
        extra_kwargs = {"password": {"write_olny": True}}

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs["email"])
        if email_exists:
            raise ValidationError("Email already exists")
        return super().validate(attrs)


class RetrieveProductsSerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ["id", "email", "products"]  # Include other fields as needed
        # extra_kwargs = {
        #     "result": {"required": False},  # Not required
        #     "user": {
        #         "required": False
        #     },  # Not required (assumed this will be set later)
        # }
