from django.urls import path
from .views import register_customer
from .views import register_wallet
from .views import register_currency
from .views import register_account
from .views import register_transaction
from .views import register_card
from .views import register_thirdparty
from .views import register_reward
from .views import register_loan
from .views import register_notifications
from .views import register_receipts

urlpatterns = [
    path('register/', register_customer, name='registration'),
    path('wallet/', register_wallet, name='wallet'),
    path('cards/', register_card, name = 'cards'),
    path('thirdparty/',register_thirdparty, name = 'thirdparty'),
    path('reward/', register_reward, name='reward'),
    path('loan/', register_loan, name = 'loan'),
    path('notification/', register_notifications, name = 'notification'),
    path('receipt/', register_receipts, name = 'receipt'),
    path('currency/', register_currency, name='currencyForm'),
    path('account/', register_account, name='account'),
    path('transaction/',register_transaction, name = 'transaction'),


]