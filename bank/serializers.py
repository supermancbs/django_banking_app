from django.contrib.auth.models import User, Withdrawl, Deposit, Transaction
from rest_framework import serializers

class WithdrawlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdrawl
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
