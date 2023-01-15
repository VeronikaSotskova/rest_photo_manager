from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from django_filters import rest_framework as filters

from src.apps.api.filters import PhotoUserFilter
from src.apps.api.serializers import PhotoUserSerializer
from src.apps.core.models import PhotoUser


class PhotoUserViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = PhotoUserSerializer
    filterset_class = PhotoUserFilter
    queryset = PhotoUser.objects.all()
    permission_classes = [AllowAny, ]
    filter_backends = (filters.DjangoFilterBackend,)
