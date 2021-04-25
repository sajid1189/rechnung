from rest_framework import routers, serializers, viewsets

from invoice.models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = '__all__'