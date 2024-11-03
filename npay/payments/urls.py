# payments/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    AccountViewSet,
    TransactionViewSet,
    ReversalRequestViewSet,
    AdminViewSet,
    AccountLinkingViewSet,
)

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"accounts", AccountViewSet)
router.register(r"transactions", TransactionViewSet)
router.register(r"reversal-requests", ReversalRequestViewSet)
router.register(r"admins", AdminViewSet)
router.register(r"account-linking", AccountLinkingViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
