from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Company, Bank, BankAccount, Branch, Department

class CoreModelTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(code="CMP01", name="Test Company", currency="USD")
        self.bank = Bank.objects.create(name="Test Bank", code="TB01")
        self.bank_account = BankAccount.objects.create(
            bank=self.bank, company=self.company, account_number="12345", account_type="Checking"
        )
        self.branch = Branch.objects.create(company=self.company, name="Main Branch", code="B01")
        self.department = Department.objects.create(company=self.company, name="HR", code="HR01")

    def test_company_creation(self):
        self.assertEqual(self.company.name, "Test Company")
        self.assertEqual(str(self.company), "Test Company")

    def test_bank_creation(self):
        self.assertEqual(self.bank.name, "Test Bank")
        self.assertEqual(str(self.bank), "Test Bank")

    def test_bank_account_creation(self):
        self.assertEqual(self.bank_account.account_number, "12345")
        self.assertEqual(str(self.bank_account), "Test Bank - 12345")

    def test_branch_creation(self):
        self.assertEqual(self.branch.name, "Main Branch")
        self.assertEqual(str(self.branch), "Test Company - Main Branch")

    def test_department_creation(self):
        self.assertEqual(self.department.name, "HR")
        self.assertEqual(str(self.department), "Test Company - HR")

class CoreAPITest(APITestCase):
    def setUp(self):
        self.company = Company.objects.create(code="CMP02", name="API Company", currency="EUR")

    def test_get_companies(self):
        url = reverse('company-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_create_company(self):
        url = reverse('company-list')
        data = {'code': 'CMP03', 'name': 'New Company', 'currency': 'GBP'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 2)
