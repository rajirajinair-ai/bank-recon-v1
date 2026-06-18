import csv
import io
from .models import BankTransaction, ImportBatch

def parse_csv_statement(file_content, bank_account, batch):
    """
    Mock parser for a CSV bank statement.
    Expects columns: Date, Description, Reference, Amount, Type
    """
    decoded_file = file_content.read().decode('utf-8')
    io_string = io.StringIO(decoded_file)
    reader = csv.DictReader(io_string)

    transactions_created = 0
    for row in reader:
        # Note: robust validation is omitted for brevity
        BankTransaction.objects.create(
            bank_account=bank_account,
            import_batch=batch,
            date=row.get('Date'),
            description=row.get('Description'),
            reference_number=row.get('Reference'),
            amount=row.get('Amount'),
            transaction_type=row.get('Type', 'DR')
        )
        transactions_created += 1

    return transactions_created
