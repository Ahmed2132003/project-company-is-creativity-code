# accounts/forms.py
from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['account', 'expense_for', 'paid_by', 'amount', 'reason']
