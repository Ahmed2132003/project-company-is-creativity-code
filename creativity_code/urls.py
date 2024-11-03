from django.urls import path, include
from home import views as main_views
from home.views import login_view, register_view
from django.contrib import admin
urlpatterns = [
    path('admin/',admin.site.urls),
    path('home/', main_views.homepage, name='homepage'),
    path('home/employees/', include('employees.urls')),
    path('home/clients/', include('clients.urls')),
    path('home/services/', include('services.urls')),
    path('home/transactions/', include('transactions.urls')),
    path('home/accounts/', include('accounts.urls')),
    path('home/about/', include('about.urls')),
    path('home/login/', login_view, name='login'),
    path('home/register/', register_view, name='register'),

]
