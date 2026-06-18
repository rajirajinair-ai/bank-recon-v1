from django.db import models
from accounts.models import User
from transactions.models import ReconciliationGroup

class ApprovalWorkflow(models.Model):
    reconciliation_group = models.OneToOneField(ReconciliationGroup, on_delete=models.CASCADE, related_name='workflow')
    current_state = models.CharField(max_length=50, default='DRAFT') # DRAFT, PREPARED, REVIEWED, APPROVED
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Workflow for {self.reconciliation_group}"

class ApprovalAction(models.Model):
    workflow = models.ForeignKey(ApprovalWorkflow, on_delete=models.CASCADE, related_name='actions')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=50) # APPROVE, REJECT, SEND_BACK
    comments = models.TextField(blank=True, null=True)
    action_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} by {self.user} on {self.action_date}"
