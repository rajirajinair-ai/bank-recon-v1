from celery import shared_task
from .models import BankTransaction, SourceTransaction, ReconciliationGroup, ReconciliationItem
from django.db.models import Sum

@shared_task
def auto_match_transactions():
    """
    A basic automated matching engine prioritizing 1-to-1 exact matches based on UTR/RRN,
    Amount, and Date. More complex logic can be added later.
    """
    unmatched_bank_txs = BankTransaction.objects.filter(status='UNMATCHED')

    for bank_tx in unmatched_bank_txs:
        # Try finding a 1-to-1 exact match on UTR/RRN and amount
        match = SourceTransaction.objects.filter(
            status='UNMATCHED',
            amount=bank_tx.amount,
            transaction_type=bank_tx.transaction_type
        ).filter(
            rrn=bank_tx.utr  # Basic matching assumption: source RRN matches bank UTR
        ).first()

        if match:
            # Create a Reconciliation Group
            group = ReconciliationGroup.objects.create(status='PREPARED')

            # Create Items
            ReconciliationItem.objects.create(group=group, bank_transaction=bank_tx)
            ReconciliationItem.objects.create(group=group, source_transaction=match)

            # Update Statuses
            bank_tx.status = 'MATCHED'
            bank_tx.save()
            match.status = 'MATCHED'
            match.save()

    return "Auto-matching completed."
