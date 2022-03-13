from typing import List

import strawberry

from . import types


@strawberry.type
class Query:
    banks: List[types.Bank] = strawberry.django.field()
    accounts: List[types.Account] = strawberry.django.field()
