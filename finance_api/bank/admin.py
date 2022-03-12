from django.contrib import admin

from finance_api.bank import models


# Register your models here.
@admin.register(models.Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(models.Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ["id", "bank", "name", "alias", "type"]


@admin.register(models.Snapshot)
class SnapshotAdmin(admin.ModelAdmin):
    list_display = ["id", "account", "date", "amount"]


@admin.register(models.Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ["datetime", "account_from", "account_to", "amount"]


@admin.register(models.Withdraw)
class WithdrawAdmin(admin.ModelAdmin):
    list_display = ["datetime", "account", "amount"]


@admin.register(models.Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ["datetime", "account", "amount"]
