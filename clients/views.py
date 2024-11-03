# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Clintes

def Client_list(request):
    clints = Clintes.objects.all()
    return render(request, 'clients/Clients_list.html', {'clints': clints})

# عرض صفحة إضافة موظف
def Add_client(request):
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        number_of_transection = request.POST['number_of_transection']
        first_transction = request.POST['first_transction']
        # التحقق من وجود البريد الإلكتروني بالفعل
        if Clintes.objects.filter(email=email).exists():
            messages.error(request, 'البريد الإلكتروني موجود بالفعل.')
        else:
            # إضافة موظف جديد
            Clintes.objects.create(
                id=id,
                name=name,
                email=email,
                phone_number=phone_number,
                number_of_transection=number_of_transection,
                first_transction=first_transction,
            )
            messages.success(request, 'تم إضافة العميل بنجاح!')
            return redirect('clients:Client_list')  
    return render(request, 'clients/Add_clients.html')

# عرض صفحة تعديل موظف
def edit_clients(request, pk):
    clients = get_object_or_404(Clintes, pk=pk)

    if request.method == 'POST':
        clients.id = request.POST['id']
        clients.name = request.POST['name']
        clients.email = request.POST['email']
        clients.phone_number = request.POST['phone_number']
        clients.number_of_transection = request.POST['number_of_transection']
        clients.first_transction = request.POST['first_transction']
        clients.save()
        messages.success(request, 'تم تعديل بيانات العميل بنجاح!')
        return redirect('clients:Client_list')

    return render(request, 'clients/edit_clients.html', {'clients': clients})

# حذف موظف
def delete_client(request, pk):
    clients = get_object_or_404(Clintes, pk=pk)
    clients.delete()
    messages.success(request, 'تم حذف العميل بنجاح!')
    return redirect('clients:Client_list')
