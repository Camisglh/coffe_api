from rest_framework import serializers
from .models import Card, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("The name must be at least 3 characters")
        return value

    def validate_description(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Description must be at least 3 characters"
            )
        return value


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("The name must be at least 3 characters")
        return value

    def validate_description(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Description must be at least 3 characters"
            )
        return value

    def validate_price(self, value):
        if not isinstance(value, (int, float)):
            raise serializers.ValidationError("Price must be a number")
        return value
