from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Employee

# عرض قائمة الموظفين
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

# عرض صفحة إضافة موظف
def add_employee(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        job_title = request.POST['job_title']
        hire_date = request.POST['hire_date']
        employment_type = request.POST['employment_type']
        
        # التحقق من وجود البريد الإلكتروني بالفعل
        if Employee.objects.filter(email=email).exists():
            messages.error(request, 'البريد الإلكتروني موجود بالفعل.')
        else:
            # إضافة موظف جديد
            Employee.objects.create(
                name=name,
                email=email,
                phone_number=phone_number,
                job_title=job_title,
                hire_date=hire_date,
                employment_type=employment_type
            )
            messages.success(request, 'تم إضافة الموظف بنجاح!')
            return redirect('employee_list')  # تأكد من تعديل هذا الاسم ليتناسب مع رابط قائمة الموظفين

    return render(request, 'employees/add_employee.html')

# عرض صفحة تعديل موظف
def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.phone_number = request.POST['phone_number']
        employee.job_title = request.POST['job_title']
        employee.hire_date = request.POST['hire_date']
        employee.employment_type = request.POST['employment_type']
        employee.save()
        messages.success(request, 'تم تعديل بيانات الموظف بنجاح!')
        return redirect('employee_list')

    return render(request, 'employees/edit_employee.html', {'employee': employee})

# حذف موظف
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    messages.success(request, 'تم حذف الموظف بنجاح!')
    return redirect('employee_list')
