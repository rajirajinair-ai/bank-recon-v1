from django.db import models
from accounts.models import User
from transactions.models import BankTransaction

class ReportRequest(models.Model):
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    report_type = models.CharField(max_length=100)
    parameters = models.JSONField()
    status = models.CharField(max_length=50, default='PENDING') # PENDING, PROCESSING, COMPLETED, FAILED
    file_path = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.report_type} by {self.requested_by}"

class SystemSetting(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.key

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100, blank=True, null=True)
    object_id = models.CharField(max_length=50, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} by {self.user} at {self.timestamp}"

class TDSEntry(models.Model):
    bank_transaction = models.ForeignKey(BankTransaction, on_delete=models.CASCADE, related_name='tds_entries')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    tds_type = models.CharField(max_length=50) # TDS_ON_INTEREST, CUSTOMER_TDS
    date = models.DateField()

    def __str__(self):
        return f"TDS: {self.amount} for {self.bank_transaction}"

class InterestEntry(models.Model):
    bank_transaction = models.ForeignKey(BankTransaction, on_delete=models.CASCADE, related_name='interest_entries')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    interest_type = models.CharField(max_length=50) # SAVINGS, FD
    date = models.DateField()

    def __str__(self):
        return f"Interest: {self.amount} for {self.bank_transaction}"
