from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

from . import views
from django.urls import path
from .views import SearchResultsView

urlpatterns = [path('', views.main, name="main"),
               path('register/', views.register, name='register'),
               path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
               path('profile/', views.profile, name='profile'),
               path('employee/', views.employee, name='employee'),
               path('employee_main/', views.employee_main, name='employee_main'),
               path('inventar_forms/', views.inventar_forms, name='inventar_forms'),
               path('employee_forms/', views.employee_forms, name='employee_forms'),
               path('category_forms/', views.category_forms, name='category_forms'),
               path('inventar/', views.inventar, name='inventar'),
               path('inventar_AZ/', views.inventar_AZ, name='inventar_AZ'),
               path('inventar_ZA/', views.inventar_ZA, name='inventar_ZA'),
               path('inventar_price/', views.inventar_price, name='inventar_price'),
               path('inventar_reprice/', views.inventar_reprice, name='inventar_reprice'),
               path('search/', SearchResultsView, name='search_results'),
               path('inventar_detail/<int:category_id>', views.inventar_detail, name='inventar_detail'),
               path('inventar/<int:pk>', views.MyDetailView1.as_view(), name='detail'),
               path('categories/', views.categories, name='categories'),

               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
