from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

from . import views
from django.urls import path



urlpatterns = [path('', views.main, name="main"),
               path('register/',views.register, name='register'),
               path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
               path('profile/', views.profile, name='profile'),
               path('employee/', views.employee, name='employee'),
               path('inventar_forms/', views.inventar_forms, name='inventar_forms'),
               path('employee_forms/', views.employee_forms, name='employee_forms'),
               path('inventar/', views.inventar, name='inventar'),
               path('<slug:slug>/', views.MyDetailView1.as_view(), name='detail'),

               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
