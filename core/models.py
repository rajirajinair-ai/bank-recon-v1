from django.db import models

class Company(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    gst_number = models.CharField(max_length=15, blank=True, null=True)
    pan_number = models.CharField(max_length=10, blank=True, null=True)
    currency = models.CharField(max_length=3, default="INR")

    def __str__(self):
        return self.name

class Branch(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='branches')
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.company.name} - {self.name}"

class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.company.name} - {self.name}"

class Bank(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class BankAccount(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='accounts')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='bank_accounts')
    account_number = models.CharField(max_length=50, unique=True)
    account_type = models.CharField(max_length=50)
    currency = models.CharField(max_length=3, default="INR")
    opening_balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.bank.name} - {self.account_number}"
