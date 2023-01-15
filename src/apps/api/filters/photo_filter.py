from django_filters import rest_framework as filters

from src.apps.core.models import Photo


class PhotoFilter(filters.FilterSet):
    name = filters.CharFilter(label="Имя человека", method='filter_name')
    date_created__lte = filters.DateFilter(label="Дата до", field_name='date_created', lookup_expr='lte')
    date_created__gte = filters.DateFilter(label="Дата от", field_name='date_created', lookup_expr='gte')

    def filter_name(self, queryset, name, value):
        return queryset.filter(names__name=value)

    class Meta:
        model = Photo
        fields = ('x', 'y', 'name', 'date_created__lte', 'date_created__gte')
