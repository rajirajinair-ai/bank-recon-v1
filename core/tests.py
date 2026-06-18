from django.test import TestCase
from .models import Company

class CompanyModelTest(TestCase):
    def setUp(self):
        Company.objects.create(code="CMP01", name="Test Company", currency="USD")

    def test_company_creation(self):
        company = Company.objects.get(code="CMP01")
        self.assertEqual(company.name, "Test Company")
        self.assertEqual(company.currency, "USD")
