from django.db import transaction
from rest_framework import serializers

from src.apps.core.models import PhotoUser, Photo


class PhotoUploadSerializer(serializers.ModelSerializer):
    user_names = serializers.ListField(
        child=serializers.CharField(max_length=255),
        allow_null=True,
        allow_empty=True,
        required=False
    )

    class Meta:
        model = Photo
        fields = ('id', 'file', 'user_names', 'x', 'y', 'description')

    def create(self, validated_data):
        user_names = []
        if 'user_names' in validated_data:
            user_names = validated_data['user_names'][0].split(',')
            del validated_data['user_names']
        user = self.context.get('request').user
        validated_data['user'] = user
        instance = super().create(validated_data)

        photo_users = []

        with transaction.atomic():
            for user_name in user_names:
                photo_user, created = PhotoUser.objects.get_or_create(
                    name=user_name
                )
                photo_users.append(photo_user)
        instance.names.set(photo_users)

        return instance

    def to_representation(self, instance):
        instance.user_names = instance.names.values_list('name', flat=True)
        representation = super().to_representation(instance)
        return representation
