import django_filters
from .models import *

class Items_Filter(django_filters.FilterSet):
    status = django_filters.CharFilter(method='filter_by_status')
    class Meta:
        model=Item
        fields=["status"]

    def filter_by_status(self, queryset, name, value):
        current_time = timezone.now()
        if value == "Running":
            return queryset.filter(start_date__lte=timezone.now(), end_date__gt=timezone.now())
        elif value == "Pending":
            return queryset.filter(start_date__gt=timezone.now())
        elif value == "Closed":
            return queryset.filter(end_date__lt=current_time)
        else:
            return queryset