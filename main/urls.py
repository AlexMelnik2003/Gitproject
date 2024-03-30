from . import views
from django.urls import path

urlpatterns = [path('', views.index, name="index"),
               path('registr/', views.UserRegister.as_view()),
               ]