from bank.models import User, Withdrawal, Deposit, Transaction
from rest_framework import viewsets
from bank.serializers import UserSerializer, WithdrawalSerializer, DepositSerializer, TransactionSerializer
import pdb; pdb.set_trace()

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer


class WithdrawalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Withdrawal.objects.all().order_by('created_at')
    serializer_class = WithdrawalSerializer

class DepositViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Deposit.objects.all().order_by('created_at')
    serializer_class = DepositSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Transaction.objects.all().order_by('created_at')
    serializer_class = TransactionSerializer
