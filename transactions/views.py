from rest_framework import viewsets
from .models import BankTransaction, SourceTransaction
from .serializers import BankTransactionSerializer, SourceTransactionSerializer

class BankTransactionViewSet(viewsets.ModelViewSet):
    queryset = BankTransaction.objects.all()
    serializer_class = BankTransactionSerializer

class SourceTransactionViewSet(viewsets.ModelViewSet):
    queryset = SourceTransaction.objects.all()
    serializer_class = SourceTransactionSerializer
