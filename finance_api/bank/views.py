from django.shortcuts import HttpResponse
from finance_api.utils import bank_utils

# Create your views here.
def information(request):
    data = bank_utils.need_to_finalize()
    return HttpResponse(data)
