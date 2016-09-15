from bank.models import User, Withdrawal, Deposit, Transaction
from rest_framework import serializers

class WithdrawalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdrawal
        fields = ('amount', 'created_at')

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ('amount', 'created_at')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('amount', 'created_at')

class UserSerializer(serializers.ModelSerializer):
    tracks = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ('name', 'amount', 'withdrawls', 'deposits', 'recieved_money', 'sent_money')
