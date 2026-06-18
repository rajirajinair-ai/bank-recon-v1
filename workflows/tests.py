from django.test import TestCase
from accounts.models import User
from transactions.models import ReconciliationGroup
from .models import ApprovalWorkflow, ApprovalAction

class WorkflowsModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="approver", password="123")
        self.recon_group = ReconciliationGroup.objects.create(created_by=self.user)
        self.workflow = ApprovalWorkflow.objects.create(reconciliation_group=self.recon_group)
        self.action = ApprovalAction.objects.create(
            workflow=self.workflow, user=self.user, action="APPROVE", comments="Looks good"
        )

    def test_workflow_creation(self):
        self.assertTrue("Workflow for Recon Group" in str(self.workflow))

    def test_action_creation(self):
        self.assertTrue("APPROVE by approver" in str(self.action))
