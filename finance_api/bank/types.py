import strawberry
from strawberry.django import auto

from . import models


@strawberry.django.type(models.Bank)
class Bank:
    id: auto
    name: auto


@strawberry.django.type(models.Account)
class Account:
    id: auto
    name: auto
    bank: Bank
    amount: auto
    last_updated: auto


@strawberry.django.type(models.Transaction)
class Transaction:
    id: auto
    account_from: Account
    account_to: Account
    amount: auto
    datetime: auto


@strawberry.django.type(models.Withdraw)
class Withdraw:
    id: auto
    account: Account
    amount: auto
    datetime: auto


@strawberry.django.type(models.Deposit)
class Deposit:
    id: auto
    account: Account
    amount: auto
    datetime: auto
