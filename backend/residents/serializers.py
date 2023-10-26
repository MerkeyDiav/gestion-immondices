from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Resident

User = get_user_model()


class ResidentSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Resident
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "street",
            "postal_number",
            "phone_number",
            "born_date",
        )

    def create(self, validated_data):
        password1 = validated_data.pop("password1")
        password2 = validated_data.pop("password2")

        if password1 != password2:
            raise serializers.ValidationError("Passwords do not match")

        user = User.objects.create_user(**validated_data)
        user.set_password(password1)
        user.save()

        return user
