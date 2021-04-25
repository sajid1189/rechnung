import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rechnung.settings")

import django
django.setup()
from invoice.models import *

# contract1 = Contract.objects.create(contract_number='1234')
# contract2 = Contract.objects.create(contract_number='1235')
#
# invoice11 = Invoice.objects.create(invoice_number=11, contract=contract1)
# invoice12 = Invoice.objects.create(invoice_number=12, contract=contract1)
#
# invoice21 = Invoice.objects.create(invoice_number=21, contract=contract2)
# invoice22 = Invoice.objects.create(invoice_number=22, contract=contract2)

contract = Contract.objects.create(contract_number='1235')
invoice22 = Invoice.objects.create(invoice_number=22, contract=contract)