# transactions/forms.py
from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount_paid', 'transaction_status']

    def clean_amount_paid(self):
        amount_paid = self.cleaned_data['amount_paid']
        service_price = self.instance.service_request.service.price
        if amount_paid > service_price:
            raise forms.ValidationError("Amount paid cannot exceed the service price.")
        return amount_paid
