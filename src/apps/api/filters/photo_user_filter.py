from django_filters import rest_framework as filters

from src.apps.core.models import PhotoUser


class PhotoUserFilter(filters.FilterSet):
    name = filters.CharFilter(label="Имя человека", field_name='name', lookup_expr='istartswith')

    class Meta:
        model = PhotoUser
        fields = ('name',)
