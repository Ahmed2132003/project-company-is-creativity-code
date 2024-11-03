# transactions/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Transaction
from .forms import TransactionForm

# عرض قائمة المعاملات
def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/transaction_list.html', {'transactions': transactions})

# عرض تعديل معاملة
def edit_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)

    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transactions:transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'transactions/edit_transaction.html', {'form': form, 'transaction': transaction})

# عرض حذف معاملة
def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transactions:transaction_list')
    return render(request, 'transactions/delete_transaction.html', {'transaction': transaction})
