from rest_framework import serializers
from .models import BankTransaction, SourceTransaction

class BankTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankTransaction
        fields = '__all__'

class SourceTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceTransaction
        fields = '__all__'
