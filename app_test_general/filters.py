import django_filters
from django_filters import CharFilter
from .models import table_filter_model


class CoworkerFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = table_filter_model
        fields = '__all__'
        exclude = [
            'date_time_created',
        ]
