# accounts/views.py
from django.shortcuts import render, redirect
from .models import Account, Expense
from .forms import ExpenseForm

def account_summary(request):
    account = Account.objects.first()  # نفترض وجود حساب واحد
    context = {
        'account': account,
        'expenses': account.expenses.all() if account else [],
    }
    return render(request, 'accounts/account_summary.html', context)

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:account_summary')
    else:
        form = ExpenseForm()
    return render(request, 'accounts/add_expense.html', {'form': form})
