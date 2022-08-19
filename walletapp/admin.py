from django.contrib import admin
from .models import Customer,Wallet,Account,Currency,Transaction,Card,ThirdParty ,Receipts,Loan,Reward,Notifications
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','age','email',)
    search_fields=('first_name','last_name',)
admin.site.register(Account)
admin.site.register(Customer)
admin.site.register(Receipts)
admin.site.register(Currency)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(Notifications)
admin.site.register(ThirdParty)
admin.site.register(Wallet)
admin.site.register(Reward)
admin.site.register(Loan)

