# services/urls.py

from django.urls import path
from .views import request_service, service_list, service_requests, edit_service_request, delete_service_request

app_name = 'services'

urlpatterns = [
    path('service_list/', service_list, name='service_list'),
    path('request/<int:service_id>/', request_service, name='request_service'),
    path('requests/', service_requests, name='service_requests'),
    path('requests/edit/<int:request_id>/', edit_service_request, name='edit_service_request'),
    path('requests/delete/<int:request_id>/', delete_service_request, name='delete_service_request'),
]
