from typing import List

import strawberry

from . import types


@strawberry.type
class Query:
    banks: List[types.Bank] = strawberry.django.field()
    accounts: List[types.Account] = strawberry.django.field()
    transactions: List[types.Transaction] = strawberry.django.field()
    withdraws: List[types.Withdraw] = strawberry.django.field()
    deposits: List[types.Deposit] = strawberry.django.field()
