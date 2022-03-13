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
