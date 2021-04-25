import django_filters

from invoice.models import Invoice


class ListFilter(django_filters.Filter):
    def filter(self, qs, value):
        value = value.split(',') if value else []
        return super().filter(qs, value)


class InvoiceFilter(django_filters.FilterSet):
    contract = ListFilter(field_name='contract__id', lookup_expr='in')
    creation_date = django_filters.DateFilter()
    billed = django_filters.BooleanFilter(field_name='billed', lookup_expr='isnull', exclude=True)

    class Meta:
        model = Invoice
        fields = ['contract', 'creation_date', 'billed']
