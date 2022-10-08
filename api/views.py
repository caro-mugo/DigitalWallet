from django.shortcuts import render
from rest_framework import viewsets
from walletapp.models import Account, Card, Customer, Loan,Notifications, Receipts, Reward, ThirdParty, Transaction, Wallet
from .serializers import AccountSerializer, CardSerializer, CustomerSerializer, LoanSerializer,NotificationsSerializer, ReceiptSerializer, RewardSerializer, ThirdpartySerializer, TransactionSerializer, WalletSerializer

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
    
class AccountViewset(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class=AccountSerializer

class WalletViewset(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class=WalletSerializer

class ReceiptViewset(viewsets.ModelViewSet):
    queryset = Receipts.objects.all()
    serializer_class=ReceiptSerializer

class CardViewset(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class=CardSerializer

class ThirdpartyViewset(viewsets.ModelViewSet):
    queryset = ThirdParty.objects.all()
    serializer_class=ThirdpartySerializer

class NotificationsViewset(viewsets.ModelViewSet):
    queryset =Notifications.objects.all()
    serializer_class=NotificationsSerializer


class LoanViewset(viewsets.ModelViewSet):
    queryset =Loan.objects.all()
    serializer_class=LoanSerializer

class RewardViewset(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class=RewardSerializer

class TransactionViewset(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class=TransactionSerializer
        