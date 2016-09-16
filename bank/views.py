from bank.models import User, Withdrawal, Deposit, Transaction
from rest_framework import viewsets
from bank.serializers import UserSerializer, WithdrawalSerializer, DepositSerializer, TransactionSerializer
from django.http import JsonResponse

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer

def create(request):
    user = User.objects.create(name=request['name'], phone_number=request[phone_number], address=request[address], balance=request[balance])
    return JsonResponse(user)




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
