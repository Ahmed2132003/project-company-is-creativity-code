# accounts/urls.py
from django.urls import path
from .views import account_summary, add_expense

app_name = 'accounts'

urlpatterns = [
    path('', account_summary, name='account_summary'),
    path('add-expense/', add_expense, name='add_expense'),
]
