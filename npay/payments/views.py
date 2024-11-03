# payments/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User, Account, Transaction, ReversalRequest, Admin, AccountLinking
from .serializers import (
    UserSerializer,
    AccountSerializer,
    TransactionSerializer,
    ReversalRequestSerializer,
    AdminSerializer,
    AccountLinkingSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class AccountViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing account instances.
    """

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]


class TransactionViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing transaction instances.
    """

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]


class ReversalRequestViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing reversal request instances.
    """

    queryset = ReversalRequest.objects.all()
    serializer_class = ReversalRequestSerializer
    permission_classes = [IsAuthenticated]


class AdminViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing admin instances.
    """

    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticated]


class AccountLinkingViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing account linking instances.
    """

    queryset = AccountLinking.objects.all()
    serializer_class = AccountLinkingSerializer
    permission_classes = [IsAuthenticated]
