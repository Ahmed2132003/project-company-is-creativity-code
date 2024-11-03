# services/models.py

from django.db import models
from  clients.models import Clintes
class Service(models.Model):
    SERVICE_CHOICES = [
        ('web_development', 'Web Development'),
        ('mobile_app', 'Mobile Apps'),
        ('desktop_app', 'Desktop Apps'),
        ('ai_model', 'AI Model Programming'),
        ('data_analysis', 'Data Analysis'),
        ('scripts', 'Scripts'),
        ('web_scraping', 'Web Scraping and Data Collection'),
        ('subscription', 'Subscription System with Company'),
    ]

    level = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class ServiceRequest(models.Model):
    customer = models.ForeignKey(Clintes, on_delete=models.CASCADE, related_name='service_requests')  # إضافة related_name
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_requests')
    is_completed = models.BooleanField(default=False)  # حالة الاكتمال
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.service.name} requested by {self.customer.name}"
