from django.test import TestCase
from accounts.models import User
from core.models import BankAccount, Bank, Company
from transactions.models import BankTransaction
from .models import ReportRequest, SystemSetting, AuditLog, TDSEntry, InterestEntry
from .tasks import generate_report

class ReportsModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="reportuser", password="123")
        self.company = Company.objects.create(code="R_CMP", name="Report Company")
        self.bank = Bank.objects.create(name="R_Bank", code="RB")
        self.bank_account = BankAccount.objects.create(
            bank=self.bank, company=self.company, account_number="5555", account_type="Checking"
        )
        self.bank_tx = BankTransaction.objects.create(
            bank_account=self.bank_account, date="2023-01-01", description="Test", amount=100.00, transaction_type="CR"
        )

        self.report_req = ReportRequest.objects.create(
            requested_by=self.user, report_type="Reconciliation", parameters={"date": "2023-01-01"}
        )
        self.setting = SystemSetting.objects.create(key="MAX_RETRIES", value="3")
        self.audit = AuditLog.objects.create(user=self.user, action="LOGIN")
        self.tds = TDSEntry.objects.create(bank_transaction=self.bank_tx, amount=10.00, tds_type="CUSTOMER_TDS", date="2023-01-01")
        self.interest = InterestEntry.objects.create(bank_transaction=self.bank_tx, amount=5.00, interest_type="SAVINGS", date="2023-01-01")

    def test_report_request_creation(self):
        self.assertTrue("Reconciliation by reportuser" in str(self.report_req))

    def test_system_setting_creation(self):
        self.assertEqual(str(self.setting), "MAX_RETRIES")

    def test_audit_log_creation(self):
        self.assertTrue("LOGIN by reportuser" in str(self.audit))

    def test_tds_entry_creation(self):
        self.assertTrue("TDS: 10.0" in str(self.tds))

    def test_interest_entry_creation(self):
        self.assertTrue("Interest: 5.0" in str(self.interest))

class ReportsTasksTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="reportuser2", password="123")
        self.report_req = ReportRequest.objects.create(
            requested_by=self.user, report_type="Summary", parameters={"month": "01"}
        )

    def test_generate_report_task(self):
        result = generate_report(self.report_req.id)

        self.assertEqual(result, f"Report {self.report_req.id} generated.")

        self.report_req.refresh_from_db()
        self.assertEqual(self.report_req.status, "COMPLETED")
        self.assertTrue(self.report_req.file_path.endswith(".csv"))

    def test_generate_report_task_not_found(self):
        result = generate_report(9999)
        self.assertEqual(result, "Report not found.")
