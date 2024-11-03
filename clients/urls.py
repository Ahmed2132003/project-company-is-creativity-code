# urls.py

from django.urls import path
from .views import Client_list, Add_client, edit_clients, delete_client

app_name = 'clients'  # إضافة مساحة الاسم هنا

urlpatterns = [
    path('', Client_list, name='Client_list'),
    path('add/', Add_client, name='Add_client'),
    path('edit/<int:pk>/', edit_clients, name='edit_clients'),
    path('delete/<int:pk>/', delete_client, name='delete_client'),
]
