# accounts/admin.py
from django.contrib import admin
from .models import Account, Expense

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('total_income', 'total_expense', 'net_profit')

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('expense_for', 'paid_by', 'amount', 'reason', 'expense_date')
