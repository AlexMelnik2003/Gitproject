from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import RegisterForm
from .models import Employee, Inventar
from django.shortcuts import render
from django.views.generic import DetailView, CreateView


def main(request):
    return render(request, "main.html")



class UserRegister(CreateView):
    model = User
    template_name = 'registration/reg.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')


class MyDetailView(DetailView):
    model = Inventar
    template_name = 'detail/detail.html'
    context_object_name = 'inventar'
    slug_field = 'slug'

@login_required
def employee(request):
    employee = Employee.objects.all()
    return render(request, 'employee.html', {'employee': employee})

@login_required
def inventar1(request):
    inventar = Inventar.objects.all()
    return render(request, 'inventar.html', {'inventar': inventar})
