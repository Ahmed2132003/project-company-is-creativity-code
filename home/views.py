from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

# عرض الصفحة الرئيسية
def homepage(request):
    return render(request, 'home/homepage.html')

# عرض صفحة تسجيل الدخول
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')  # تعديل 'homepage' حسب اسم الصفحة الرئيسية
        else:
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة')
    
    return render(request, 'home/login.html')

# عرض صفحة التسجيل
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # تحقق من وجود اسم المستخدم
        if User.objects.filter(username=username).exists():
            messages.error(request, 'اسم المستخدم موجود بالفعل')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'تم إنشاء الحساب بنجاح، يمكنك الآن تسجيل الدخول')
            return redirect('login')  # تعديل 'login' حسب اسم صفحة تسجيل الدخول
    
    return render(request, 'home/register.html')
