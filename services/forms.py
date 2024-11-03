# services/forms.py

from django import forms
from .models import Service

class ServiceRequestForm(forms.Form):
    service_id = forms.ModelChoiceField(queryset=Service.objects.all(), label="Select Service")
    client_name = forms.CharField(max_length=100, label="Client Name")
