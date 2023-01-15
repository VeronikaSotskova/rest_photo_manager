from rest_framework import serializers

from src.apps.core.models import Photo


class PhotoWithoutMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'file')
