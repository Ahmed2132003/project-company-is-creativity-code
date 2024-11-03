# services/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import Service ,ServiceRequest
from clients.models import Clintes
from .models import Service
from clients.models import Clintes
from transactions.models import Transaction
from decimal import Decimal
def service_list(request):
    services = Service.objects.all().order_by('category', 'level')
    return render(request, 'services/service_list.html', {'services': services})
def request_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        
        try:
            customer = Clintes.objects.get(name=customer_name)
            # حفظ الطلب في جدول ServiceRequest
            service_request = ServiceRequest(customer=customer, service=service)
            service_request.save()
            Transaction.objects.create(
                service_request=service_request,
                amount_paid=Decimal('0.00'),  # استخدام `Decimal` بدلاً من `0.00`
                transaction_status='25%'  # حالة افتراضية عند 25%
            )
            return redirect('services:service_requests')   # انتقل إلى صفحة عرض الطلبات
        except Clintes.DoesNotExist:
            error_message = "Customer does not exist. Please register before requesting a service."
            return render(request, 'services/request_service.html', {'service': service, 'error_message': error_message})

    return render(request, 'services/request_service.html', {'service': service})

# services/views.py

def service_requests(request):
    
    requests = ServiceRequest.objects.all()
    filter_option = request.GET.get('filter')
    if filter_option == 'completed':
        requests = ServiceRequest.objects.filter(is_completed=True)
    elif filter_option == 'not_completed':
        requests = ServiceRequest.objects.filter(is_completed=False)
    else:
        requests = ServiceRequest.objects.all()

    return render(request, 'services/service_requests.html', {'requests': requests})

def edit_service_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)

    if request.method == 'POST':
        # تعديل الخدمة المطلوبة
        service_id = request.POST['service_id']
        service_request.service = get_object_or_404(Service, id=service_id)
        service_request.is_completed = request.POST.get('is_completed', False)
        service_request.save()
        return redirect('services:service_requests')

    services = Service.objects.all()
    return render(request, 'services/edit_service_request.html', {'service_request': service_request, 'services': services})

def delete_service_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    service_request.delete()
    return redirect('services:service_requests')
