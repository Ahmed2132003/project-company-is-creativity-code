from django.db import models
from django.utils import timezone
from services.models import Service, ServiceRequest
from decimal import Decimal, InvalidOperation

class Transaction(models.Model):
    service_request = models.OneToOneField(ServiceRequest, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))  # المبلغ المدفوع
    amount_remaining = models.DecimalField(max_digits=10, decimal_places=2)  # المبلغ المتبقي
    transaction_date = models.DateTimeField(default=timezone.now)  # تاريخ المعاملة
    STATUS_CHOICES = [
        ('25%', '25%'),
        ('50%', '50%'),
        ('75%', '75%'),
        ('100%', '100%'),
    ]
    transaction_status = models.CharField(max_length=4, choices=STATUS_CHOICES, default='25%')  # حالة المعاملة

    def save(self, *args, **kwargs):
        try:
            from accounts.models import Account

            # تحويل `service.price` إلى `Decimal`
            service_price = Decimal(str(self.service_request.service.price))
            self.amount_remaining = service_price - self.amount_paid

            account, created = Account.objects.get_or_create(id=1)  # افتراض حساب واحد
            account.total_income += self.amount_paid
            account.calculate_net_profit()
        except (TypeError, InvalidOperation) as e:
            # تسجيل أو طباعة رسالة خطأ توضح المشكلة
            raise ValueError(f"Error converting service price to Decimal: {e}")
        
        super().save(*args, **kwargs)