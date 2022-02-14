from django_filters import FilterSet, AllValuesFilter, NumberFilter,DateRangeFilter,DateFilter,CharFilter

from accounts.models import Client


class ClientFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')
    start_date = DateFilter(field_name='created_at',lookup_expr=('gt'),)
    end_date = DateFilter(field_name='created_at',lookup_expr=('lt'))
    date_range = DateRangeFilter(field_name='created_at')
    class Meta:
        model = Client
        fields = ['created_at','name']
