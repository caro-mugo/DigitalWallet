from dataclasses import fields
from rest_framework import serializers
from walletapp.models import Account, Card, Customer, Loan, Notifications, Receipts, Reward, ThirdParty, Transaction, Wallet 



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("first_name", "email", "age")
        
        
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model= Account
        fields=('account_number','account_type','balance','name',)

class  WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model= Wallet
        fields=('currency','customer','balance','date','status','pin')

class  ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model= Receipts
        fields=('transaction', 'receipt_date','recipt_number','account','receipt_type')

class  CardSerializer(serializers.ModelSerializer):
    class Meta:
        model= Card
        fields=('cvv_security','expiry_date','card_name','card_type','card_number','card_status','date_Issued')   


class  ThirdpartySerializer(serializers.ModelSerializer):
    class Meta:
        model= ThirdParty
        fields=('thirdparty_id','phone_Number','currency','name','account')             


class  NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Notifications
        fields=('notification_Id','date','status','recipient') 
        
class  LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model= Loan
        fields=('loan_type','loan_number','amount','date','wallet','interest_rate','due_date','loan_balance','loan_term')       

class  RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model= Reward
        fields=('transaction','date','customer')  
        
        
class  TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Transaction
        fields=('transaction_type','transaction_amount','transaction_date','transaction_charge','wallet')  
        
