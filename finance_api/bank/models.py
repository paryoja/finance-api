from django.db import models


# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class AccountType(models.TextChoices):
    SAVINGS_ACCOUNT = "SAVINGS_ACCOUNT", "자유입출금"
    INSTALLMENT_SAVING = "INSTALLMENT_SAVING", "적금"
    TIME_DEPOSIT = "TIME_DEPOSIT", "예금"


class Account(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(
        max_length=30, choices=AccountType.choices, default=AccountType.SAVINGS_ACCOUNT
    )

    def __str__(self):
        return self.bank.name + ":" + self.name


class Snapshot(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField()


class Transaction(models.Model):
    account_from = models.ForeignKey(
        Account, related_name="account_from", on_delete=models.CASCADE
    )
    account_to = models.ForeignKey(
        Account, related_name="account_to", on_delete=models.CASCADE
    )
    amount = models.PositiveIntegerField()
    datetime = models.DateTimeField()
    note = models.TextField(null=True, blank=True)


class Withdraw(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    datetime = models.DateTimeField()
    note = models.TextField()


class Deposit(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    datetime = models.DateTimeField()
    note = models.TextField()
