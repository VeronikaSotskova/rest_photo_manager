from rest_framework import mixins
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from django_filters import rest_framework as filters

from src.apps.api.filters import PhotoFilter
from src.apps.api.serializers import PhotoUploadSerializer, PhotoWithoutMetadataSerializer
from src.apps.api.v1.mixins import SerializerByActionMixin, PermissionsByActionMixin
from src.apps.core.models import Photo


class PhotoViewSet(PermissionsByActionMixin, SerializerByActionMixin, mixins.CreateModelMixin, mixins.ListModelMixin,
                   mixins.RetrieveModelMixin, GenericViewSet):
    permission_classes = [AllowAny, ]
    permissions_by_action = {
        'create': [IsAuthenticated, ]
    }

    serializer_class = PhotoUploadSerializer
    serializer_class_by_action = {
        'list': PhotoWithoutMetadataSerializer
    }

    parser_classes = (MultiPartParser,)

    queryset = Photo.objects.all().prefetch_related('names')

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PhotoFilter
