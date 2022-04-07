from dataclasses import fields
from rest_framework import serializers

from .models import Item


class SearchSerializer(serializers.Serializer):
    search = serializers.CharField(max_length=256)


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
