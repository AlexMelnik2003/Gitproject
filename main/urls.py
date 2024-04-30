from django.contrib.auth.views import LoginView


from . import views
from django.urls import path

from .views import UserRegister

urlpatterns = [path('', views.main, name="main"),
               path('register/', UserRegister.as_view(template_name='registration/reg.html'), name='register'),
               path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
               path('employee/', views.employee, name='employee'),
               path('inventar_forms/', views.inventar_forms, name='inventar_forms'),
               path('employee_forms/', views.employee_forms, name='employee_forms'),
               path('inventar/', views.inventar, name='inventar'),
               path('<slug:slug>/', views.MyDetailView1.as_view(), name='detail'),

               ]
