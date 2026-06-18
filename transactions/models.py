from django.db import models
from core.models import BankAccount
from accounts.models import User

class ImportBatch(models.Model):
    file_name = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, default='PENDING') # PENDING, PROCESSING, COMPLETED, FAILED

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.file_name

class BankTransaction(models.Model):
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name='transactions')
    import_batch = models.ForeignKey(ImportBatch, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    description = models.TextField()
    reference_number = models.CharField(max_length=100, blank=True, null=True)
    utr = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_type = models.CharField(max_length=10) # DR or CR
    status = models.CharField(max_length=50, default='UNMATCHED') # UNMATCHED, MATCHED, PARTIALLY_MATCHED

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.date} - {self.amount} ({self.transaction_type})"

class SourceTransaction(models.Model):
    source_type = models.CharField(max_length=50) # UPI, CARD, PAYROLL, AP, AR, TAX, GATEWAY
    date = models.DateField()
    description = models.TextField()
    reference_number = models.CharField(max_length=100, blank=True, null=True)
    rrn = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_type = models.CharField(max_length=10) # DR or CR
    status = models.CharField(max_length=50, default='UNMATCHED') # UNMATCHED, MATCHED, PARTIALLY_MATCHED

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.source_type} - {self.date} - {self.amount}"

class ReconciliationGroup(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, default='DRAFT') # DRAFT, PREPARED, REVIEWED, APPROVED

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"Recon Group {self.id}"

class ReconciliationItem(models.Model):
    group = models.ForeignKey(ReconciliationGroup, on_delete=models.CASCADE, related_name='items')
    bank_transaction = models.ForeignKey(BankTransaction, on_delete=models.SET_NULL, null=True, blank=True)
    source_transaction = models.ForeignKey(SourceTransaction, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"Item in {self.group}"
