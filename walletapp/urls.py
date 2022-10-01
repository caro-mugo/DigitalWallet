from django.urls import path
from .views import  customer_profile, edit_profile, list_accounts, list_cards, list_currencys, list_customers, list_loans, list_notifications, list_receipts, list_rewards, list_thirdpartys, list_transactions, list_wallets 
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
    path('customers/',list_customers,name='customers_list'),
    path('wallets/',list_wallets,name='wallets_list'),
    path('thirdpartys/',list_thirdpartys,name='thirdpartys_list'),
    path('receipts/',list_receipts,name='receipts_list'),
    path('transactions/',list_transactions,name='transactions_list'),
    path('transactions/',list_cards,name='cards_list'),
    path('notifications/',list_notifications,name='notifications_list'),
    path('loans/',list_loans,name='loans_list'),
    path('rewards/',list_rewards,name='rewards_list'),
    path('currencys/',list_currencys,name='currencys_list'),
    path('accounts/',list_accounts,name='accounts_list'),
    
    path("customerrs/<int:id>/", customer_profile,name="customer_profile"),
    path("customerrs/edit/<int:id>/", edit_profile,name="edit_profile"),

    








]

    