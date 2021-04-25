from datetime import datetime

from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from invoice.factories import ContractFactory, InvoiceFactory
from invoice.models import Invoice
from invoice.serializers import InvoiceSerializer


class InvoiceViews(APITestCase):

    @classmethod
    def setUpTestData(cls):
        today = datetime.now().date()
        cls.contract1 = ContractFactory()
        cls.contract2 = ContractFactory()
        cls.contract3 = ContractFactory()

        cls.invoice11 = InvoiceFactory(contract=cls.contract1, draft=True)
        cls.invoice21 = InvoiceFactory(contract=cls.contract1, creation_date=today)

        cls.invoice12 = InvoiceFactory(contract=cls.contract2)
        cls.invoice22 = InvoiceFactory(contract=cls.contract2, billed=None)
        cls.invoice32 = InvoiceFactory(contract=cls.contract2, creation_date=today)

        cls.invoice13 = InvoiceFactory(contract=cls.contract3, billed=None)

    def _get_ids_from_response(self, response):
        return [i['id'] for i in response.json()]

    def test_details_view(self):
        response = self.client.get(reverse('invoice-detail', kwargs={"pk": self.invoice11.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(InvoiceSerializer(self.invoice11).data, response.json())

    def test_view_partial_update(self):
        self.assertTrue(self.invoice11.draft)
        response = self.client.patch(reverse('invoice-detail', kwargs={"pk": self.invoice11.id}),
                                     data={"draft": False})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(InvoiceSerializer(self.invoice11).data, response.json())

        self.invoice11.refresh_from_db()
        self.assertFalse(self.invoice11.draft)

    def test_filter_by_single_contract(self):
        url = f"{reverse('invoice-list')}?contract={self.contract2.id}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_inv_ids = [self.invoice12.id, self.invoice22.id, self.invoice32.id]
        self.assertCountEqual(expected_inv_ids, self._get_ids_from_response(response))

    def test_filter_by_multiple_contracts(self):
        url = f"{reverse('invoice-list')}?contract={self.contract2.id},{self.contract3.id}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_inv_ids = [self.invoice12.id, self.invoice22.id, self.invoice32.id, self.invoice13.id]
        self.assertCountEqual(expected_inv_ids, self._get_ids_from_response(response))

    def test_filter_by_creation_date(self):
        today = datetime.now().date()
        url = f"{reverse('invoice-list')}?creation_date={today}"
        response = self.client.get(url)
        expected_inv_ids = [self.invoice21.id, self.invoice32.id]
        self.assertCountEqual(expected_inv_ids, self._get_ids_from_response(response))

    def test_filter_by_billed(self):
        today = datetime.now().date()
        url = f"{reverse('invoice-list')}?billed={True}"
        response = self.client.get(url)
        expected_inv_ids = Invoice.objects.filter(billed__isnull=False).values_list('id', flat=True)
        self.assertCountEqual(expected_inv_ids, self._get_ids_from_response(response))










