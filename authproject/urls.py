from django.contrib import admin
from django.urls import path
from authapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.register, name='register'),
    path('log_in/', views.log_in, name='log_in'),
    path('dashboard/', views.dashboard, name='dashboard')
]
