from django.contrib import admin
from .models import Customer,Wallet,Account,Currency,Transaction,Card,ThirdParty ,Receipts,Loan,Reward,Notifications
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','age','email',)
    search_fields=('first_name','last_name',)
admin.site.register(Customer,CustomerAdmin)
class AccountAdmin(admin.ModelAdmin):
    list_display=('account_number','account_type','balance','name',)
    search_fields=('first_name','last_name',)
admin.site.register(Account,AccountAdmin)
# admin.site.register(Account)
# admin.site.register(Customer)
# admin.site.register(Receipts)
# admin.site.register(Currency)
# admin.site.register(Transaction)
# admin.site.register(Card)
# admin.site.register(Notifications)
# admin.site.register(ThirdParty)
# admin.site.register(Wallet)
# admin.site.register(Reward)
# admin.site.register(Loan)


class CurrencyAdmin(admin.ModelAdmin):
    list_display=('amount','country_of_origin')
    search_fields=('first_name','last_name',)
admin.site.register(Currency,CurrencyAdmin)
class TransactionAdmin(admin.ModelAdmin):
    list_display=('transaction_type','transaction_amount','transaction_date','transaction_charge','wallet')
    search_fields=('first_name','last_name',)
admin.site.register(Transaction,TransactionAdmin)
class CardAdmin(admin.ModelAdmin):
    list_display=('cvv_security','expiry_date','card_name','card_type','card_number','card_status','date_Issued')
    search_fields=('first_name','last_name',)
admin.site.register(Card,CardAdmin)
class NotificationsAdmin(admin.ModelAdmin):
    list_display=('notification_Id','date','status','recipient')
    search_fields=('first_name','last_name',)
admin.site.register(Notifications,NotificationsAdmin)   
class ThirdPartyAdmin(admin.ModelAdmin):
    list_display=('thirdparty_id','phone_Number','currency','name','account')
    search_fields=('first_name','last_name',)
admin.site.register(ThirdParty,ThirdPartyAdmin)
class WalletAdmin(admin.ModelAdmin):
    list_display=('currency','customer','balance','date','status','pin')
    search_fields=('first_name','last_name',)
admin.site.register(Wallet,WalletAdmin)
class RewardAdmin(admin.ModelAdmin):
    list_display=('transaction','date','customer')
    search_fields=('first_name','last_name',)
admin.site.register(Reward,RewardAdmin)
class LoanAdmin(admin.ModelAdmin):
    list_display=('loan_type','loan_number','amount','date','wallet','interest_rate','due_date','loan_balance','loan_term')
    search_fields=('first_name','last_name',)
admin.site.register(Loan,LoanAdmin)
class ReceiptsAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'receipt_date','recipt_number','account','receipt_type')
    search_fields = ('first_name', 'last_name')
admin.site.register(Receipts, ReceiptsAdmin)
