from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Pokemon

CustomUser = get_user_model()


class PokemonSerializer(serializers.ModelSerializer):
    def validate_height_cm(self, value):
        if value <= 0:
            raise serializers.ValidationError("Height in cm must be a positive number")
        return value

    def validate_weight_kg(self, value):
        if value <= 0:
            raise serializers.ValidationError("Weight in kg must be a positive number")
        return value

    def create(self, validated_data):
        validated_data["discovered_by"] = self.context["request"].user
        return Pokemon.objects.create(**validated_data)

    class Meta:
        model = Pokemon
        exclude = ["discovered_by"]

class PokemonUpdateSerializer(serializers.ModelSerializer):
    def validate_height_cm(self, value):
        if value <= 0:
            raise serializers.ValidationError("Height in cm must be a positive number")
        return value

    def validate_weight_kg(self, value):
        if value <= 0:
            raise serializers.ValidationError("Weight in kg must be a positive number")
        return value

    def update(self, instance, validated_data):
        instance.description = validated_data.get("description", instance.description)
        instance.height_cm = validated_data.get("height_cm", instance.height_cm)
        instance.weight_kg = validated_data.get("weight_kg", instance.weight_kg)
        instance.type = validated_data.get("type", instance.type)
        instance.save()
        return instance

    class Meta:
        model = Pokemon
        exclude = ["discovered_by", "name"]



class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    class Meta:
        model = CustomUser
        fields = ["email", "password"]

    def create(self, validated_data):
        user = CustomUser.objects.create(email=validated_data["email"])
        user.set_password(validated_data["password"])
        user.save()
        return user
