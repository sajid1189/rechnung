from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from invoice.utils.date_utils import start_of_period_date, end_of_period_date


class Invoice(models.Model):
    invoice_number = models.IntegerField(_("Rechnungsnummer"), default=0)
    file_name = models.CharField(
        _("Rechnungsname"), max_length=256, blank=True, default=""
    )
    creation_date = models.DateField(_("Rechnungsdatum"), default=timezone.now)
    payment_target_date = models.DateField(_("Zahlbar bis"), blank=True, null=True)
    cancellation_date = models.DateField(_("Storniert am"), blank=True, null=True)
    period_start = models.DateField(
        _("Abrechnungsperiode von"), default=start_of_period_date
    )
    period_end = models.DateField(_("Abrechnungsperiode bis"), default=end_of_period_date)
    counter_start = models.FloatField(_("Zählerstartwert"), blank=True, null=True)
    counter_end = models.FloatField(_("Zählerendwert"), default=0)
    net_sum = models.DecimalField(
        _("Rechnungsbetrag (Netto)"), max_digits=12, decimal_places=4, default=0
    )
    billed = models.DateField(_("Abgerechnet am"), blank=True, null=True, default=None)
    contract = models.ForeignKey('Contract', on_delete=models.SET_NULL, null=True)
    invoice_update = models.ForeignKey(
        "self", blank=True, null=True, on_delete=models.SET_NULL
    )
    draft = models.BooleanField(_("Entwurf"), default=False)


class Contract(models.Model):
    contract_label = models.CharField(max_length=256, default=_("Hauptzähler"))
    contract_number = models.CharField(max_length=256)
    contract_details = models.TextField(blank=True, null=True)
