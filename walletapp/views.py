from django.shortcuts import render
from .forms import CustomerRegistrationForm
from .forms import WalletRegistrationForm
from .forms import CurrencyRegistrationForm
from .forms import AccountRegistrationForm
from .forms import ThirdPartyRegistrationForm
from .forms import ReceiptsRegistrationForm
from .forms import TransactionRegistrationForm
from .forms import CardRegistrationForm
from .forms import NotificationsRegistrationForm
from .forms import LoanRegistrationForm
from .forms import RewardRegistrationForm

def register_customer(request):
    form = CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{"form": form})
def register_wallet(request):
    form = WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html",{"form":form})
def register_thirdparty(request):
    form = ThirdPartyRegistrationForm()
    return render(request,"wallet/register_thirdparty.html",{"form":form})

def register_receipts(request):
    form = ReceiptsRegistrationForm()
    return render(request,"wallet/register_receipt.html",{"form":form})

def register_transaction(request):
    form = TransactionRegistrationForm()
    return render(request,"wallet/register_transaction.html",{"form":form})

def register_card(request):
    form = CardRegistrationForm()
    return render(request,"wallet/register_card.html",{"form":form})

def register_notifications(request):
    form = NotificationsRegistrationForm()
    return render(request,"wallet/register_notification.html",{"form":form})

def register_loan(request):
    form = LoanRegistrationForm()
    return render(request,"wallet/register_loan.html",{"form":form})

def register_reward(request):
    form = RewardRegistrationForm()
    return render(request,"wallet/register_reward.html",{"form":form})    

def register_currency(request):
    form = CurrencyRegistrationForm()
    return render(request,"wallet/register_currency.html",{"form":form})

def register_account(request):
    form = AccountRegistrationForm()
    return render(request,"wallet/register_account.html",{"form":form})



# Create your views here.
