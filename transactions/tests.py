from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import BankTransaction, SourceTransaction, ImportBatch, ReconciliationGroup, ReconciliationItem
from core.models import Bank, BankAccount, Company
from accounts.models import User
from .tasks import auto_match_transactions

class TransactionsModelTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(code="T_CMP", name="Transaction Company")
        self.bank = Bank.objects.create(name="T_Bank", code="TB")
        self.bank_account = BankAccount.objects.create(
            bank=self.bank, company=self.company, account_number="9876", account_type="Savings"
        )
        self.user = User.objects.create_user(username="txuser", password="123")
        self.batch = ImportBatch.objects.create(file_name="test.csv", uploaded_by=self.user)

        self.bank_tx = BankTransaction.objects.create(
            bank_account=self.bank_account, import_batch=self.batch,
            date="2023-01-01", description="Test Tx", amount=100.00, transaction_type="CR"
        )
        self.source_tx = SourceTransaction.objects.create(
            source_type="UPI", date="2023-01-01", description="Source Tx", amount=100.00, transaction_type="CR"
        )
        self.recon_group = ReconciliationGroup.objects.create(created_by=self.user)
        self.recon_item = ReconciliationItem.objects.create(
            group=self.recon_group, bank_transaction=self.bank_tx, source_transaction=self.source_tx
        )

    def test_import_batch_creation(self):
        self.assertEqual(str(self.batch), "test.csv")

    def test_bank_transaction_creation(self):
        self.assertEqual(str(self.bank_tx), "2023-01-01 - 100.0 (CR)")

    def test_source_transaction_creation(self):
        self.assertEqual(str(self.source_tx), "UPI - 2023-01-01 - 100.0")

    def test_reconciliation_group_creation(self):
        self.assertTrue("Recon Group" in str(self.recon_group))

    def test_reconciliation_item_creation(self):
        self.assertTrue("Item in" in str(self.recon_item))

class TransactionsAPITest(APITestCase):
    def setUp(self):
        self.company = Company.objects.create(code="T_CMP2", name="Transaction Company 2")
        self.bank = Bank.objects.create(name="T_Bank2", code="TB2")
        self.bank_account = BankAccount.objects.create(
            bank=self.bank, company=self.company, account_number="1111", account_type="Savings"
        )
        self.bank_tx = BankTransaction.objects.create(
            bank_account=self.bank_account, date="2023-01-02", description="API Tx", amount=50.00, transaction_type="DR"
        )

    def test_get_bank_transactions(self):
        url = reverse('banktransaction-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

class TransactionsTasksTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(code="T_CMP3", name="Transaction Company 3")
        self.bank = Bank.objects.create(name="T_Bank3", code="TB3")
        self.bank_account = BankAccount.objects.create(
            bank=self.bank, company=self.company, account_number="2222", account_type="Savings"
        )
        # Create matching transactions
        self.bank_tx = BankTransaction.objects.create(
            bank_account=self.bank_account, date="2023-01-03", description="Match Bank",
            amount=200.00, transaction_type="CR", utr="RRN123", status="UNMATCHED"
        )
        self.source_tx = SourceTransaction.objects.create(
            source_type="GATEWAY", date="2023-01-03", description="Match Source",
            amount=200.00, transaction_type="CR", rrn="RRN123", status="UNMATCHED"
        )

        # Create non-matching transaction
        self.bank_tx_no_match = BankTransaction.objects.create(
            bank_account=self.bank_account, date="2023-01-03", description="No Match Bank",
            amount=50.00, transaction_type="CR", utr="RRN999", status="UNMATCHED"
        )

    def test_auto_match_transactions_task(self):
        # Execute Celery task synchronously for testing
        result = auto_match_transactions()

        self.assertEqual(result, "Auto-matching completed.")

        # Verify the matching logic worked
        self.bank_tx.refresh_from_db()
        self.source_tx.refresh_from_db()
        self.bank_tx_no_match.refresh_from_db()

        self.assertEqual(self.bank_tx.status, "MATCHED")
        self.assertEqual(self.source_tx.status, "MATCHED")
        self.assertEqual(self.bank_tx_no_match.status, "UNMATCHED")

        # Verify ReconciliationGroup and Item were created
        groups = ReconciliationGroup.objects.all()
        self.assertEqual(groups.count(), 1)
        self.assertEqual(groups.first().items.count(), 2)
