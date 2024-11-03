# accounts/models.py
from django.db import models
from transactions.models import Transaction  # تعديل لاستيراد موديل المعاملات
from decimal import Decimal
from django.utils import timezone
class Account(models.Model):
    total_income = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'))  # إجمالي الدخل
    total_expense = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'))  # إجمالي الخارج
    net_profit = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'))  # صافي الربح

    def calculate_net_profit(self):
        self.net_profit = self.total_income - self.total_expense
        self.save()

class Expense(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='expenses')
    expense_for = models.CharField(max_length=255)  # الخارج لصالح
    paid_by = models.CharField(max_length=255)  # الخارج من
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # المبلغ الخارج
    reason = models.TextField()  # السبب
    expense_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        # تحديث إجمالي الخارج في حساب الشركة
        if self.account:
            self.account.total_expense += self.amount
            self.account.calculate_net_profit()
        super().save(*args, **kwargs)
