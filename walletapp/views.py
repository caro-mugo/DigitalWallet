from locale import currency

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
from django.shortcuts import render,redirect

from .models import Account, Card, Currency, Customer, Loan, Notifications, Receipts, Reward, ThirdParty, Transaction, Wallet



def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{"form": form})

def list_customers(request):
    customer=Customer.objects.all()
    return render(request,"wallet/customers_list.html",{"Customer": customer})


# customer profile
def customer_profile(request,id):
    customer = Customer.objects.get(id=id)
    return render(request,"wallet/customer_profile.html",{"customer":customer})

def edit_profile(request,id):
    customer = Customer.objects.get(id=id)
    if request.method=="POST":
        form = CustomerRegistrationForm(request.POST,instance=Customer)
        if form.isvalid():
            form.save()
            return redirect("Customer_profile",id=customer.id)
    else:
        form = CustomerRegistrationForm(instance=Customer)
        return render(request,"wallet/edit_profile.html",{"form":form})

       
def register_wallet(request):
    if request.method == 'POST':
        form = WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html",{"form":form})

def list_wallets(request):
    wallet=Wallet.objects.all()
    return render(request,"wallet/wallets_list.html",{"Wallet": wallet})
       

def register_thirdparty(request):
    if request.method == 'POST':
        form = ThirdPartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ThirdPartyRegistrationForm()
    return render(request,"wallet/register_thirdparty.html",{"form":form})

def list_thirdpartys(request):
    thirdparty=ThirdParty.objects.all()
    return render(request,"wallet/thirdpartys_list.html",{"ThirdParty": thirdparty})
       

def register_receipts(request):
    if request.method == 'POST':
        form = ReceiptsRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ReceiptsRegistrationForm()
    return render(request,"wallet/register_receipts.html",{"form":form})

def list_receipts(request):
    receipts=Receipts.objects.all()
    return render(request,"wallet/receipts_list.html",{"Receipts": receipts})
    
    

def register_transaction(request):
    if request.method == 'POST':
        form = TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form=TransactionRegistrationForm()
    return render(request,"wallet/register_transaction.html",{"form":form})

def list_transactions(request):
    transaction=Transaction.objects.all()
    return render(request,"wallet/transactions_list.html",{"Transaction": transaction})
    

def register_card(request):
    if request.method == 'POST':
        form = CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form=CardRegistrationForm()
    return render(request,"wallet/register_card.html",{"form":form})

def list_cards(request):
    card=Card.objects.all()
    return render(request,"wallet/cards_list.html",{"Card": card})    

def register_notifications(request):
    if request.method == 'POST':
        form = NotificationsRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form=NotificationsRegistrationForm()
    return render(request,"wallet/register_notifications.html",{"form":form})

def list_notifications(request):
    notifications=Notifications.objects.all()
    return render(request,"wallet/notifications_list.html",{"Notifications": notifications})     
    

def register_loan(request):
    if request.method == 'POST':
        form = LoanRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form=LoanRegistrationForm()
    return render(request,"wallet/register_loan.html",{"form":form})

def list_loans(request):
    loan=Loan.objects.all()
    return render(request,"wallet/loans_list.html",{"Loan": loan})   

def register_reward(request):
    if request.method == 'POST':
        form = RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form=RewardRegistrationForm()
    return render(request,"wallet/register_reward.html",{"form":form})

def list_rewards(request):
    reward=Reward.objects.all()
    return render(request,"wallet/rewards_list.html",{"Reward": reward})      

def register_currency(request):
    if request.method == 'POST':
        form = CurrencyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form=CurrencyRegistrationForm()
    return render(request,"wallet/register_currency.html",{"form":form})
def list_currencys(request):
    currency=Currency.objects.all()
    return render(request,"wallet/currencys_list.html",{"Currency": currency})
    

def register_account(request):
    if request.method == 'POST':
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form=AccountRegistrationForm()
    return render(request,"wallet/register_account.html",{"form":form})

def list_accounts(request):
    account=Account.objects.all()
    return render(request,"wallet/accounts_list.html",{"Account": account})    

def edit_transaction(request, id):
    transact = Transaction.objects.get(id=id)
    if request.method == 'POST':
        form = TransactionRegistrationForm(request.POST, instance=transact)
        if form.is_valid():
            form.save()
            return redirect('profile', id=transact.id)

    else:
        form = CardRegistrationForm(instance=transact)
        return render(request, 'wallet/edit_transact.html', {'form': form})

def edit_receipt(request, id):
    receipt = Receipts.objects.get(id=id)
    if request.method == 'POST':
        form = ReceiptsRegistrationForm(request.POST, instance=receipt)
        if form.is_valid():
            form.save()
            return redirect('profile', id=receipt.id)

    else:
        form = ReceiptsRegistrationForm(instance=receipt)
        return render(request, 'wallet/edit_receipt.html', {'form': form})

def edit_card(request, id):
    card = Card.objects.get(id=id)
    if request.method == 'POST':
        form = CardRegistrationForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('profile', id=card.id)

    else:
        form = CardRegistrationForm(instance=card)
        return render(request, 'wallet/edit_card.html', {'form': form})
    
def edit_wallet(request, id):
    wallet = Wallet.objects.get(id=id)
    if request.method == 'POST':
        form = WalletRegistrationForm(request.POST, instance=wallet)
        if form.is_valid():
            form.save()
            return redirect('profile', id=wallet.id)

    else:
        form = WalletRegistrationForm(instance=wallet)
        return render(request, 'wallet/edit_wallet.html', {'form': form})

def edit_account(request, id):
    account = Account.objects.get(id=id)
    if request.method == 'POST':
        form = AccountRegistrationForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('profile', id=account.id)

    else:
        form = AccountRegistrationForm(instance=account)
        return render(request, 'wallet/edit_account.html', {'form': form})    
    
def edit_profile(request,id):
     
    customer=Customer.objects.get(id=id)
    if request.method =="POST":
        form=CustomerRegistrationForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customer_profile",id=customer.id)
    else:
        form=CustomerRegistrationForm(instance=customer)
        return render(request,"wallet/edit_profile.html",{"form":form}) 
       
def wallet_profile(request,id):
    wallet = Wallet.objects.get(id=id)
    return render(request, 'wallet/wallet_profile.html',{'wallet': wallet})

def receipt_profile(request,id):
    receipt =Receipts.objects.get(id=id)
    return render(request, 'wallet/receipt_profile.html',{'receipt': receipt})

def transaction_profile(request,id):
   transaction =Transaction.objects.get(id=id)
   return render(request, 'wallet/transaction_profile.html',{'transaction': transaction})

def account_profile(request,id):
  account =Account.objects.get(id=id)
  return render(request, 'wallet/account_profile.html',{'account': account})

def card_profile(request,id):
    card =Card.objects.get(id=id)
    return render(request, 'wallet/card_profile.html',{'card': card})




    

# Create your views here.
