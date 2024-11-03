from django.urls import path
from . import views

app_name = 'transactions'

urlpatterns = [
    path('list/', views.transaction_list, name='transaction_list'),  # عرض قائمة المعاملات
    path('edit/<int:transaction_id>/', views.edit_transaction, name='edit_transaction'),  # تعديل معاملة
    path('delete/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),  # حذف معاملة
]
