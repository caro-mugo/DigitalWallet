from email.policy import default
from django.db import models
from django.forms import DateTimeField
from django.utils import timezone

# Create your models here.

class Account(models.Model):
    account_number=models.IntegerField(default=0)
    account_type=models.CharField(max_length=15,null=True)
    balance=models.IntegerField()
    name=models.CharField(max_length=20,null=True)
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE, related_name ='Account_wallet')

class Wallet(models.Model):
    currency =models.ForeignKey('Currency', on_delete=models.CASCADE, related_name ='Wallet_currency')
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE, related_name ='Wallet_customer')
    balance=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=15,null=True)
    pin=models.TextField(max_length=6,null=True)
    
class Customer(models.Model):
    first_name=models.CharField(max_length=10,null=True)
    last_name=models.CharField(max_length=10,null=True)
    age=models.CharField(max_length=10,null=True)
    address=models.CharField(max_length=20,null=True)
    email=models.EmailField(max_length=25,null=True)
    phonenumber=models.CharField(max_length=15,null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,null=True)
    date_created = models.DateTimeField(default=timezone.now)
    nationality=models.CharField(max_length=15,null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/',null=True)    

    
class Currency(models.Model):
    amount=models.IntegerField()
    country_of_origin=models.CharField(max_length=20,null=True) 


class Transaction(models.Model):
    transaction_ref=models.CharField(max_length=150,null=True)
    wallet=models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name   = 'Transaction_wallet')
    transaction_amount=models.IntegerField()
    TRANSACTION_CHOICES = (
       ('withdraw', 'Withdrawal'),
        ('deposit', 'deposit'),
    )
    transaction_type=models.CharField(max_length=10, choices=TRANSACTION_CHOICES,null=True)
    transaction_charge=models.IntegerField()
    transaction_date=models.DateTimeField(default=timezone.now)
    original_account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name='Transaction_original_account')
    destination_account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name='Transaction_destination_account')

class Card(models.Model):
    date_Issued=models.DateTimeField(default=timezone.now)
    card_name=models.CharField(max_length=10,null=True)
    card_number=models.IntegerField()
    ISSUER_CHOICES=(
         ('Master', 'Mastercard'),
        ('visa', 'Mastercard'),
    )
    card_type=models.CharField(max_length=10, choices=ISSUER_CHOICES,null=True)
    expiry_date=models.DateTimeField(default=timezone.now)
    STATUS_CHOICES = (
        ('d', 'debit'),
        ('d', 'credit'),
    )
    
    card_status= models.CharField(max_length=1, choices=STATUS_CHOICES,null=True)
    cvv_security=models.IntegerField()
    wallet=models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name ='Card_wallet')
    account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name ='Card_account')     

class ThirdParty(models.Model):
    account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name ='ThirdParty_account')
    name=models. CharField(max_length=15,null=True)
    thirdparty_id=models.CharField(max_length=10,null=True)
    phone_Number=models.IntegerField()
    currency=models.ForeignKey('Currency', on_delete=models.CASCADE, related_name ='ThirdParty_currency')


class Notifications(models.Model):
    notification_Id=models.CharField(max_length=25,null=True)
    STATUS_CHOICES = (
        ('read', 'read'),
        ('unread', 'unread'),
    )
    status=models.CharField(max_length=12, choices=STATUS_CHOICES,null=True)
    date=models.DateTimeField(default=timezone.now)
    recipient=models.ForeignKey('Customer', on_delete=models.CASCADE, related_name ='Notifications_recipient')    
 
class Reward(models.Model):  
    transaction=models.ForeignKey('Transaction', on_delete=models.CASCADE, related_name ='Reward_transaction')
    date=models.DateTimeField(default=timezone.now)
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE, related_name ='Reward_customer')
 


class Receipts(models.Model):
    receipt_type=models.CharField(max_length=25, null=True)
    receipt_date=models.DateTimeField(default=timezone.now)
    recipt_number=models.CharField(max_length=25, null=True)
    account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name ='Receipts_account')
    total_Amount=models.IntegerField(default=0)
    transaction=models.ForeignKey('Transaction', on_delete=models.CASCADE, related_name ='Receipts_transaction')
    recipt_File=models.FileField(upload_to='wallet')
    

class Loan(models.Model):
    interest_rate=models.IntegerField()
    guaranter=models.ForeignKey('Customer', on_delete=models.CASCADE, related_name ='guarantor')
    due_date=models.DateField(default=timezone.now)
    loan_balance=models.IntegerField()
    loan_term=models.IntegerField()
    loan_number=models.IntegerField()
    loan_type=models.CharField(max_length=25, null=True)
    amount=models.IntegerField()
    date=models.DateTimeField(default=timezone.now)
    wallet=models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name ='wallet_Loan')




