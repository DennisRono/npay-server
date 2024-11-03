from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings


# User Model
class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ("PERSONAL", "Personal"),
        ("BUSINESS", "Business"),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    linked_personal_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="linked_business_users",
    )

    groups = models.ManyToManyField(Group, related_name="custom_user_set", blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name="custom_user_permissions", blank=True
    )

    def __str__(self):
        return f"{self.username} ({self.user_type})"


# Account Model
class Account(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ("SAVINGS", "Savings"),
        ("CURRENT", "Current"),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES)
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=10, default="ACTIVE")

    def __str__(self):
        return f"{self.user.username} - {self.account_type}"


# Transaction Model
class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ("TRANSFER", "Transfer"),
        ("DEPOSIT", "Deposit"),
        ("WITHDRAWAL", "Withdrawal"),
    ]
    TRANSACTION_STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("COMPLETED", "Completed"),
        ("FAILED", "Failed"),
        ("REVERSED", "Reversed"),
    ]
    from_account = models.ForeignKey(
        Account, related_name="sent_transactions", on_delete=models.SET_NULL, null=True
    )
    to_account = models.ForeignKey(
        Account,
        related_name="received_transactions",
        on_delete=models.SET_NULL,
        null=True,
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)  # Example: 'USD', 'EUR'
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    transaction_status = models.CharField(
        max_length=10, choices=TRANSACTION_STATUS_CHOICES, default="PENDING"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} {self.currency}"


# Reversal Request Model
class ReversalRequest(models.Model):
    REVERSAL_STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
    ]
    transaction = models.ForeignKey("Transaction", on_delete=models.CASCADE)
    requesting_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="requested_reversals",
    )
    reversal_status = models.CharField(
        max_length=10, choices=REVERSAL_STATUS_CHOICES, default="PENDING"
    )
    admin = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="approved_reversals",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reversal Request for {self.transaction.id} - {self.reversal_status}"


# Admin Model
class Admin(User):  # Extend User to identify admins specifically
    role = models.CharField(max_length=50, default="Admin")

    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Admins"


# Account Linking Model
class AccountLinking(models.Model):
    business_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="business_links",
        on_delete=models.CASCADE,
    )
    personal_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="personal_links",
        on_delete=models.CASCADE,
    )
    link_status = models.CharField(max_length=10, default="ACTIVE")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Link between {self.business_user} and {self.personal_user}"
