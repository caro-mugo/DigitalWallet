from django.urls import path,include
from rest_framework import routers
from .views import AccountViewset, CardViewset, CustomerViewSet, LoanViewset,NotificationsViewset, ReceiptViewset, RewardViewset, ThirdpartyViewset, TransactionViewset, WalletViewset

router=routers.DefaultRouter()
router.register(r"customers",CustomerViewSet)
router.register (r"accounts", AccountViewset)
router.register (r"wallets", WalletViewset)
router.register (r"cards", CardViewset)
router.register (r"loans", LoanViewset)
router.register (r"thirdpartys", ThirdpartyViewset)
router.register (r"notifications", NotificationsViewset)
router.register (r"rewards", RewardViewset)
router.register (r"receipts", ReceiptViewset)
router.register (r"transactions",TransactionViewset)


urlpatterns = [
      path("",include(router.urls)),
  ]