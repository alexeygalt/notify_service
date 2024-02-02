import django_filters
from django.utils import timezone

from mailing.models import Mailing


class MailingActiveFilter(django_filters.FilterSet):
    is_active = django_filters.BooleanFilter(
        method="filter_is_active", label="Is Active"
    )

    class Meta:
        model = Mailing
        fields = ["is_active"]

    def filter_is_active(self, queryset, name, value):
        if value:
            return queryset.filter(
                start_datetime__lte=timezone.now(), end_datetime__gte=timezone.now()
            )
        return queryset.exclude(
            start_datetime__lte=timezone.now(), end_datetime__gte=timezone.now()
        )
