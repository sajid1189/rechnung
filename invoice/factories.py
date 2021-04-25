from datetime import datetime, timedelta

import factory
from factory import fuzzy
from invoice.models import Invoice, Contract


def fuzzy_start_date(offset=None):
    offset = offset if offset else 1000
    return datetime.now().date() - timedelta(days=offset)


class ContractFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contract

    contract_label = fuzzy.FuzzyText(length=10)
    contract_number = fuzzy.FuzzyText(length=100)
    contract_details = fuzzy.FuzzyText(length=200)


class InvoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Invoice

    invoice_number = fuzzy.FuzzyInteger(low=1)
    file_name = fuzzy.FuzzyText(length=10)
    creation_date = fuzzy.FuzzyDate(start_date=fuzzy_start_date())
    payment_target_date = fuzzy.FuzzyDate(start_date=fuzzy_start_date())
    cancellation_date = fuzzy.FuzzyDate(start_date=fuzzy_start_date())
    period_start = fuzzy.FuzzyDate(start_date=fuzzy_start_date())
    period_end = factory.LazyAttribute(lambda obj: obj.period_start + timedelta(days=30))
    counter_start = fuzzy.FuzzyFloat(low=2)
    counter_end = factory.LazyAttribute(lambda obj: obj.counter_start + 100)
    net_sum = fuzzy.FuzzyDecimal(low=1)
    draft = fuzzy.FuzzyChoice(choices=[True, False])
    billed = fuzzy.FuzzyDate(fuzzy_start_date())

