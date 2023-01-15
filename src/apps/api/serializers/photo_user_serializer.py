from rest_framework import serializers

from src.apps.core.models import PhotoUser


class PhotoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoUser
        fields = ('name',)
