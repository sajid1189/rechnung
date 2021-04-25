from django.utils.translation import gettext as _
from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed

from django_filters import rest_framework as filters

from invoice.filters import InvoiceFilter
from invoice.models import Invoice
from invoice.serializers import InvoiceSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = InvoiceFilter

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed('DELETE')
