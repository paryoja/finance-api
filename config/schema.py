import strawberry

from finance_api.bank import queries

schema = strawberry.Schema(query=queries.Query)
