from rest_framework import serializers
from .models import User, Account, Transaction, ReversalRequest, Admin, AccountLinking
from .models import Transaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


class ReversalRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReversalRequest
        fields = "__all__"


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"


class AccountLinkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountLinking
        fields = "__all__"
