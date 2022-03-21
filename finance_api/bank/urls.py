from django.urls import path

from finance_api.bank import views

app_name = "bank"
urlpatterns = [path("information", view=views.information)]
